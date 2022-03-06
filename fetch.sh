#!/usr/bin/env bash
for i in servername1 servername2 servername3;
do
        ssh ansible@$i "sudo tar czf messages.tar.gz /var/log/messages"
done

ansible all -m fetch -a "src=/home/ansible/messages.tar.gz dest=/tmp/messages" 
