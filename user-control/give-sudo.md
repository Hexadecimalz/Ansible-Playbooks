--- 
- name: Give Sudo Permissions
  hosts: "{{ host }}" 
  vars: 
   sudoadd:
     - user: panpan
     - user: grizz
     - user: icebear
  tasks: 
    - name: Give sudo 
      copy:
        content: '{{ item.user }} ALL=(ALL:ALL) ALL'
        dest: '/etc.sudoers.d/{{ item.user }}'
        mode: 0440
      with_items:
        - "{{ sudoadd }}" 
