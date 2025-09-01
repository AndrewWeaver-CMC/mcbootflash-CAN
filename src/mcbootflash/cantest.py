"""Command line tool for flashing firmware."""

from __future__ import annotations

import argparse
from io import StringIO
from pathlib import Path
from typing import TYPE_CHECKING, Final, TextIO

import bincopy  # type: ignore[import-untyped]
from serial import Serial, SerialException  # type: ignore[import-untyped]
import can 

def can_bootloader_tasks():
    with can.Bus(interface="socketcan", channel="can0", bitrate=500000) as bus:
        msg = can.Message(
            arbitration_id=0x67, 
            data=[0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x7, 0x8, 0x9, 0x10, 0x11], 
            is_fd=True
        )
        index = 200
        while(index != 0):
            try:
                msg.data[0] = index
                bus.send(msg)
                print(f"Message sent on {bus.channel_info}")
            except:
                print("Message failed to send")
            finally:
                index -= 1

def main(args: None | argparse.Namespace = None) -> int:
    """Entry point for CLI.

    Paramaters
    ----------
    args: None | argparse.Namespace, default=None
        `main` should normally be called with no arguments, in which case arguments are
        parsed from `sysv`. A pre-parsed argument namespace can be supplied for testing
        purposes.

    Returns
    -------
    return_code: int
        0 if no error occurred, 1 otherwise.
    """
    can_bootloader_tasks()
    
can_bootloader_tasks()


# if __name__ == "__main__":
#     sys.exit(main())
