# How to Use the `multiple-new-users.yml` Playbook
## Edit the Playbook First
Edit the file with help from the table below. 

| Variable Name  | Equivalent                                                                                         |
|----------------|----------------------------------------------------------------------------------------------------|
| uname          | Username                                                                                           |
| id             | uid (<1000 does not show up on login screen. Must be unique.)                                      |
| desc           | Comment (For Example, John Smith)                                                                  |
| member         | Set groups for the user. Wheel gives sudo access, remove sudo by specifying no wheel group present |

## Create a password hash

`ansible all -i localhost, -m debug -a "msg={{ 'mypassword' | password_hash('sha512', 'mysecretsalt') }}"`

Copy the password hash into the password line make sure it's quoted. Keep in mind, the user will be forced to update the password again
on their first login. Set a good password anyways. 

## Creating Groups

You will need to create an individual play to create any groups that you want. For example, `wheel` or `data` need to be created 
in individual plays. You cannot add a user to a group that does not exist. 

## Run the Playbook (make sure Ansible is installed on the machine) 

`sudo ansible-playbook multiple-new-users.yml -e"hosts=localhost"`

If you run the script multiple times it will always update the user password, so you may want to change this if you need to run it again
to modify a user account. 
