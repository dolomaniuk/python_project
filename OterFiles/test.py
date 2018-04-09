import autoit

# autoit.run("notepad.exe")
# autoit.win_activate_by_handle(0x0002062E)
print(autoit.control_get_handle(0x0002062E, 'Сумма'))
# print(autoit.control_get_pos_by_handle(132654))
# autoit.control_send("cashDepositTaskForm:s2_e:s2", "13.1")
# autoit.win_close("[CLASS:Notepad]")
# autoit.control_click("[Class:#32770]", "Button2")