[general]
debug = boolean(default=False)
editor = command(default=None)
merge_editor = command(default=None)
default_action = action(default=None)

[contact table]
reverse = boolean(default=False)
group_by_addressbook = boolean(default=False)
show_nicknames = boolean(default=False)
show_uids = boolean(default=True)
sort = option('first_name', 'last_name', 'formatted_name', default='first_name')
display = option('first_name', 'last_name', default='first_name')
localize_dates = boolean(default=True)
preferred_phone_number_type = string_list(default=list('pref'))
preferred_email_address_type = string_list(default=list('pref'))

[vcard]
private_objects = private_objects(default=list()))
search_in_source_files = boolean(default=False)
skip_unparsable = boolean(default=False)
preferred_version = option('3.0', '4.0', default='3.0')

[addressbooks]
  [[__many__]]
    path = string