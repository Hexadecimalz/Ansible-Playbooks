# How to run the `setup.yml` playbook 
I'm not sure if this is a bug, but this playbook is run in 2 steps: 

```
ansible-playbook setup.yml -e"client=x.x.x.x" -e"myname=newname" -u root --ask-become-pass
ansible-playbook setup.yml -e"client=x.x.x.x" -e"myname=newname" -u root --ask-pass
```

We need to run the first command to accept the SSH fingerprint into `known_hosts` 
and the second command will actually run the playbook. This is working around Ansible's default configuration, which uses `ansible` as the default user.

Our variables are simple, we add in the IP address under *client* 
and the machine's hostname is set with *myname*. 