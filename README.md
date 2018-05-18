# Port Scanner

## Overview
This tool is a ***command-line port scanner using Scapy***.

It proceed to a TCP-SYN scan for each specified port for the target ip.

This program is an example of port scanning implementation using *Scapy*. For professional uses, please consider using existing tools such as [nmap](https://nmap.org/).

## Installation and Dependencies

This tool is written with **Python 2** and so require a Python 2 interpreter.

It also relies on the **Scapy** program, please visit [the official Scapy's website](http://www.secdev.org/projects/scapy/) for installation instructions.

## Documentation

### Usage

To show the usage and the help in the command line interface, use the ```--help``` (```-h```) option.
The ip target has to be specified. The scanned port list is specified with the ```--dport``` (```-p```) option. Each port is separated by a space. *Note : for now, their is no port range (such as ```-p 22-80```) or port names/groups (such as ```-p POP3 IMAP```).*

Option can also be specified to control the request timeout (```--timeout```, the default is 2s) and the verbosity (```--verbose```).

### Results

A port can be in several states :
 - **OPEN**.
 - **CLOSED**.
 - **FILTRERED**.
 - Any combination of those states. For instance, a **OPEN|FILTERED** states means that the scanner was not able to define if the port is open or filtered.

### Examples

The following list contains some usage examples :

 - ```sudo python main.py 192.168.0.16 -p 22``` : scan the port 22 (SSH) for the specified target (192.168.0.16).
 - ```sudo python main.py 192.168.0.16 -p 80 443``` : scan the target for the standard web ports (HTTP & HTTPS).
 - ```sudo python main.py 192.168.0.16 -p 80 -t 10``` : scan the port 80 (HTTP) with an user-defined timeout (10s).

## Contributors

 - Etienne BOESPFLUG [etienne.boespflug@gmail.com].

## Licence

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

This tool has no license and is free to use.

## Disclaimer

Port scanning should be restricted to you own machines. Please consult the legislation of your country.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
