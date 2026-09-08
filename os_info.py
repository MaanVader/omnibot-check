#!/usr/bin/env python3
"""OS version information helper.

This is a SAFE diagnostic script for the authorised omnibot sandbox test.
It only reads and prints OS/platform information. It performs no network
access, no file modification, and no other side effects.
"""
import platform
import sys


def main() -> None:
    print("=== OS Version Information ===")
    print(f"platform:  {platform.platform()}")
    print(f"system:    {platform.system()}")
    print(f"release:   {platform.release()}")
    print(f"version:   {platform.version()}")
    print(f"machine:   {platform.machine()}")
    print(f"python:    {sys.version.split()[0]}")


if __name__ == "__main__":
    main()
