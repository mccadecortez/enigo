from enigo_python import Enigo

enigo = Enigo(delay_between_presses=100)

enigo.execute(
    enigo.move_mouse(10, 25, Enigo.Coordinate.Rel),
    enigo.button(Enigo.Button.Left, Enigo.Direction.Click),
    enigo.text("Hello World! here is a lot of text  ❤️"),
)
