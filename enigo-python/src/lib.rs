use enigo::{self, agent::Agent, Enigo, Settings};
use pyo3::{exceptions, prelude::*};

#[allow(unused_imports)]
use core::time;
#[allow(unused_imports)]
use std::thread;

#[pymodule]
fn enigo_python(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<NativeEnigo>()?;
    Ok(())
}

#[pyclass]
pub struct NativeEnigo {
    inner: Enigo,
    /// enigo has a sleep delay for macOS, Linux X11, but none for windows
    ///
    /// implement a thread::sleep if executing on windows
    #[allow(dead_code)]
    delay_copy: u32,
}

#[pymethods]
impl NativeEnigo {
    #[new]
    #[pyo3(signature = (option_delay=0, option_display=""))]
    pub fn new(option_delay: Option<u32>, option_display: Option<&str>) -> PyResult<Self> {
        let mut settings: Settings = Settings::default();

        if let Some(delay) = option_delay {
            settings.mac_delay = delay;
            settings.linux_delay = delay;
        }

        if let Some(display) = option_display {
            let display_str = display.to_string();
            settings.wayland_display = Some(display_str.clone());
            settings.x11_display = Some(display_str);
        }

        let enigo = Enigo::new(&settings);

        let ret = match enigo {
            Ok(value) => Ok(NativeEnigo {
                inner: value,
                delay_copy: option_delay.unwrap_or_default(),
            }),
            Err(_error) => Err(exceptions::PyException::new_err(
                "failed to initalize enigo",
            )),
        };

        ret
    }

    pub fn execute(&mut self, serialized: String) -> PyResult<()> {
        let result: Result<Vec<_>, ron::de::SpannedError> = ron::from_str(&serialized);

        match result {
            Ok(deserialized_tokens) => {
                for token in &deserialized_tokens {
                    let result = self.inner.execute(token);

                    match result {
                        Err(err) => return Err(exceptions::PyException::new_err(err.to_string())),
                        Ok(_) => {
                            #[cfg(target_os = "windows")]
                            {
                                // FIXME:? We would be sleeping on the last element too, unnecessary delay
                                thread::sleep(time::Duration::from_millis(self.delay_copy.into()));
                            }

                            continue;
                        }
                    }
                }

                Ok(())
            }
            Err(err) => Err(exceptions::PyException::new_err(err.to_string())),
        }
    }
}
