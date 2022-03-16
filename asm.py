"""
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Compilers
Module | `asm.py`

Daniel Bakas Amuchástegui\
March 15, 2022

Copyright © Compilers 2022. All rights reserved.\
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
"""

from string import Template

tpl_start_data = """
    .data
"""

tpl_start_text = """
    .text
main:
"""

tpl_addition = Template("""
$left
    sw      $$a0        0($$sp)
    addiu   $$sp        $$sp -4
$right
    lw $$t1 4($$sp)
    addiu $$sp $$sp 4
    add $$a0 $$a0 $$t1
""")

tpl_end = """
    li      $v0         10
    syscall
"""

tpl_immediate = Template("""
    li      $$a0        $immediate
""")

tpl_var = Template("""
    lw      $$a0        $name
""")

tpl_assign = Template("""
$prev
    sw      $$a0        $name
""")
