# Link Stats Logger

A logger built to capture ExpressLRS link stats. It both prints to CLI and logs to files. The `pyserial` package is needed to run this tool; see `requirements.txt`.

### Selecting UART_PORT ###
For *Windows*, set to COM ports. For example, `UART_PORT = COM1`. Find the correct one in the Device Manager.

For *Linux*, set to /dev files. For example, `UART_PORT = /dev/ttyUSB0`.
