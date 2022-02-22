# User Management Playbooks 
## 👩🧑🏽👩 How to Use the `add-users.yml` Playbook
Easy Download `wget https://raw.githubusercontent.com/Hexadecimalz/Ansible-Playbooks/master/user-control/add-users.yml`
### Edit the Playbook First
Edit the file with help from the table below. 

| Variable Name  | Equivalent                                                                                         |
|----------------|----------------------------------------------------------------------------------------------------|
| uname          | Username                                                                                           |
| id             | uid (<1000 does not show up on login screen. Must be unique.)                                      |
| desc           | Comment (For Example, John Smith)                                                                  |
| member         | Set groups for the user. Wheel gives sudo access, remove sudo by specifying no wheel group present |

### Create a Password Hash
Use the follow ad-hoc command in the terminal to create a password hash. By default the password is expired on the user account, and the user will be required to set a new password after first login. 

`ansible all -i localhost, -m debug -a "msg={{ 'mypassword' | password_hash('sha512', 'mysecretsalt') }}"`

Copy the password hash into the password line make sure it's quoted. If you prefer you can run `passwd username` for each user after the playbook executes. 

### Creating Groups
Add groups you want to create as part of the `sysgroups` variable. This play to create groups exists first. The name `groups` is an Ansible built-in variable, so we need to use something slightly more unique. 

### Run the Playbook (make sure Ansible is installed on the machine) 
1. To install Ansible run `sudo apt install ansible`
1. To run the playbook `ansible-playbook add-users.yml -e"host=localhost"`

## 👤 How to use the `remove-user.yml` Playbook 
1. Download `wget https://raw.githubusercontent.com/Hexadecimalz/Ansible-Playbooks/master/user-control/remove-users.yml`
1. Edit `remove-users.yml` changing the users you want to remove
1. Run `ansible-playbook remove-users.yml -e"host=localhost"`

## 🧙 Give sudo
Follow the instructions from the previous 2 playbooks and this should make sense. 
