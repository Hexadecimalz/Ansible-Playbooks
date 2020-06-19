# User Management Playbooks 
## How to Use the `multiple-new-users.yml` Playbook
Easy Download `wget https://raw.githubusercontent.com/Hexadecimalz/Ansible-Playbooks/master/user-control/multiple-new-users.yml`
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
You will need to create an individual play to create any groups that you want. For example, `wheel` or `data` need to be created 
in individual plays. You cannot add a user to a group that does not exist. 

To check run this command in the terminal `groups`

### Run the Playbook (make sure Ansible is installed on the machine) 
1. To install Ansible run `sudo apt install ansible`
1. To run the playbook `sudo ansible-playbook multiple-new-users.yml -e"hosts=localhost"`

## How to use the `remove-user.yml` Playbook 
1. Download `wget https://raw.githubusercontent.com/Hexadecimalz/Ansible-Playbooks/master/user-control/remove-user.yml`
1. Run `sudo ansible-playbook remove-user.yml -e"hosts=localhost"`
