""" Simple wrapper for enigo, a rust keyboard and mouse control library """

from enum import Enum
from .enigo_python import NativeEnigo

__all__ = [
    "Direction",
    "Axis",
    "Coordinate",
    "Button",
    "Token",
    "Action",
    "Enigo",
]

# MARK: Enums
# XXX: serde directives have been copied and are in reference of the enum element below


class Direction(Enum):
    """The direction of a key or button"""

    # [cfg_attr(feature = "serde", serde(alias = "P"))]
    # [cfg_attr(feature = "serde", serde(alias = "p"))]
    Press = "P"
    # [cfg_attr(feature = "serde", serde(alias = "R"))]
    # [cfg_attr(feature = "serde", serde(alias = "r"))]
    Release = "R"
    # [cfg_attr(feature = "serde", serde(alias = "C"))]
    # [cfg_attr(feature = "serde", serde(alias = "c"))]
    # [default]
    Click = "C"
    """ Equivalent to a press followed by a release """


class Axis(Enum):
    """Specifies the axis for scrolling"""

    # [cfg_attr(feature = "serde", serde(alias = "H"))]
    # [cfg_attr(feature = "serde", serde(alias = "h"))]
    Horizontal = "H"
    # [cfg_attr(feature = "serde", serde(alias = "V"))]
    # [cfg_attr(feature = "serde", serde(alias = "v"))]
    # [default]
    Vertical = "V"


class Coordinate(Enum):
    """Specifies if a coordinate is relative or absolute"""

    # [doc(alias = "Absolute")]
    # [cfg_attr(feature = "serde", serde(alias = "A"))]
    # [cfg_attr(feature = "serde", serde(alias = "a"))]
    # [default]
    Abs = "A"
    # [doc(alias = "Relative")]
    # [cfg_attr(feature = "serde", serde(alias = "R"))]
    # [cfg_attr(feature = "serde", serde(alias = "r"))]
    Rel = "R"


class Button(Enum):
    """Represents a mouse button"""

    Left = "L"
    """ Left mouse button """
    # [cfg_attr(feature = "serde", serde(alias = "L"))]
    # [cfg_attr(feature = "serde", serde(alias = "l"))]
    # [default]
    Middle = "M"
    """ Middle mouse button """
    # [cfg_attr(feature = "serde", serde(alias = "M"))]
    # [cfg_attr(feature = "serde", serde(alias = "m"))]
    Right = "R"
    """ Right mouse button """
    # [cfg_attr(feature = "serde", serde(alias = "R"))]
    # [cfg_attr(feature = "serde", serde(alias = "r"))]
    Back = "B"
    """ 4th mouse button. Typically performs the same function as `Browser_Back` """
    # [cfg(any(target_os = "windows", all(unix, not(target_os = "macos"))))]
    # [cfg_attr(feature = "serde", serde(alias = "B"))]
    # [cfg_attr(feature = "serde", serde(alias = "b"))]
    Forward = "F"
    """ 5th mouse button. Typically performs the same function as `Browser_Forward` """
    # [cfg(any(target_os = "windows", all(unix, not(target_os = "macos"))))]
    # [cfg_attr(feature = "serde", serde(alias = "F"))]
    # [cfg_attr(feature = "serde", serde(alias = "f"))]
    ScrollUp = "SU"
    """ Scroll up button. """
    # [cfg_attr(feature = "serde", serde(alias = "SU"))]
    # [cfg_attr(feature = "serde", serde(alias = "su"))]
    ScrollDown = "SD"
    """ Scroll down button. """
    # [cfg_attr(feature = "serde", serde(alias = "SD"))]
    # [cfg_attr(feature = "serde", serde(alias = "sd"))]
    ScrollLeft = "SL"
    """ Scroll left button. """
    # [cfg_attr(feature = "serde", serde(alias = "SL"))]
    # [cfg_attr(feature = "serde", serde(alias = "sl"))]
    ScrollRight = "SR"
    """ Scroll right button. """
    # [cfg_attr(feature = "serde", serde(alias = "SR"))]
    # [cfg_attr(feature = "serde", serde(alias = "sr"))]


class Token(Enum):
    """Agent will execute the action associated with the Token"""

    Text = "T"
    """ Call the [`Keyboard::text`] fn with the string as text """
    # [cfg_attr(feature = "serde", serde(alias = "T"))]
    # [cfg_attr(feature = "serde", serde(alias = "t"))]
    Key = "K"
    """ Call the [`Keyboard::key`] fn with the given key and direction """
    # [cfg_attr(feature = "serde", serde(alias = "K"))]
    # [cfg_attr(feature = "serde", serde(alias = "k"))]
    Raw = "R"
    """ Call the [`Keyboard::raw`] fn with the given keycode and direction """
    # [cfg_attr(feature = "serde", serde(alias = "R"))]
    # [cfg_attr(feature = "serde", serde(alias = "r"))]
    Button = "B"
    """ Call the [`Mouse::button`] fn with the given mouse button and direction """
    # [cfg_attr(feature = "serde", serde(alias = "B"))]
    # [cfg_attr(feature = "serde", serde(alias = "b"))]
    MoveMouse = "M"
    """ Call the [`Mouse::move_mouse`] fn. The first i32 is the value to move on """
    """ the x-axis and the second i32 is the value to move on the y-axis. The """
    """ coordinate defines if the given coordinates are absolute of relative to """
    """ the current position of the mouse. """
    # [cfg_attr(feature = "serde", serde(alias = "M"))]
    # [cfg_attr(feature = "serde", serde(alias = "m"))]
    Scroll = "S"
    """ Call the [`Mouse::scroll`] fn. """
    # [cfg_attr(feature = "serde", serde(alias = "S"))]
    # [cfg_attr(feature = "serde", serde(alias = "s"))]
    Unicode = "uni"
    # """ Specify that we want to use a unicode character """


# MARK: Enigo


class Action(str):
    """Wrapper for `str`, to give a type hint to use the static methods of `Enigo`"""


class Enigo:
    """
    Enigo lets you simulate mouse and keyboard input-events as if they were made by the actual hardware. It is available on Linux (X11), macOS and Windows.

    It can be used for testing user interfaces on different platforms, building remote control applications or just automating tasks for user interfaces unaccessible by a public API or scripting language.

    ...

    Attributes
    ----------
    Re-exports the following as static properties

    Direction

    Axis

    Coordinate

    Button

    Token

    Action

    Methods
    -------
    execute(self, *args: Action):
        Execute the `Action` args in order

    Static Methods
    --------------
    String aliases to enigo-rust tokens

    text(text: str) -> Action:

    key(key: str, direction: Direction) -> Action:

    raw(keycode: int, direction: Direction) -> Action:

    button(button: Button, direction: Direction) -> Action:

    move_mouse(x: int, y: int, coordinate: Coordinate) -> Action:

    scroll(length: int, axis: Axis) -> Action:

    unicode(text: str) -> str:
    """

    def __init__(self, delay_between_presses=0, linux_display="") -> None:
        """Create a enigo instance"""
        self.enigo = NativeEnigo(
            option_delay=delay_between_presses, option_display=linux_display
        )

    def execute(self, *args: Action):
        """Execute the `Action` args in order"""
        self.enigo.execute(f"[{','.join(args)}]")

    # re-export for convenience
    Direction = Direction
    Axis = Axis
    Coordinate = Coordinate
    Button = Button
    Token = Token
    Action = Action

    @staticmethod
    def text(text: str) -> Action:
        return f'{Token.Text.value}("{text}")'

    @staticmethod
    def key(key: str, direction: Direction) -> Action:
        return f"{Token.Key.value}({key},{direction.value})"

    @staticmethod
    def raw(keycode: int, direction: Direction) -> Action:
        return f"{Token.Raw.value}({keycode},{direction.value})"

    @staticmethod
    def button(button: Button, direction: Direction) -> Action:
        return f"{Token.Button.value}({button.value},{direction.value})"

    @staticmethod
    def move_mouse(x: int, y: int, coordinate: Coordinate) -> Action:
        return f"{Token.MoveMouse.value}({x},{y},{coordinate.value})"

    @staticmethod
    def scroll(length: int, axis: Axis) -> Action:
        return f"{Token.Scroll.value}({length},{axis.value})"

    @staticmethod
    def unicode(text: str) -> str:
        """Pass to `Key`, to press the corresponding button"""
        return f"{Token.Unicode.value}('{text}')"
