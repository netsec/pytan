# create a user (basic)
user = handler.create_user("vittles1")

# create a user that already exists
user = handler.create_user("vittles1")

# create a user and delete any existing user
user = handler.create_user("vittles1", del_exists=True)

# create a user and delete any existing user without waiting
user = handler.create_user("vittles1", del_exists=True, del_wait=0)

# create a user and provide 1 computer group name
group_names = ["dumdum"]
user = handler.create_user("vittles2", group_names=group_names)

# create a user and provide 2 computer group names
group_names = ["dumdum", "aaaa"]
user = handler.create_user("vittles3", group_names=group_names)

# create a user and provide 3 computer group names
group_names = ["dumdum", "aaaa", "All Computers"]
user = handler.create_user("vittles4", group_names=group_names)

# create a user and provide 2 good computer group names and 1 bad one
group_names = ["dumdum", "aaaa", "bad group name"]
user = handler.create_user("vittles5", group_names=group_names)

# create a user, provide 1 computer group name,
# 1 property to show in console, and 1 property to hide from console (only visible via API)
props = [
    {"name": "created by", "value": "pytan v3.0.0"},
    {"name": "something", "value": "else", "show_console": False},
]
group_names = ["dumdum"]
user = handler.create_user("vittles6", group_names=group_names, props=props)

# create a user, provide 1 computer group name,
# 1 property to show in console, and 1 property to hide from console (only visible via API),
# and add 2 roles
props = [
    {"name": "created by", "value": "pytan v3.0.0"},
    {"name": "something", "value": "else", "show_console": False},
]
roles = [
    "Content Administrator",
    "Discover User",
]
group_names = ["dumdum"]
user = handler.create_user("vittles7", group_names=group_names, props=props, roles=roles)

# modify the properties of a user, supplying two names that already exist
# with overwrite set on second one, and supplying a third name that doesn't exist
props = [
    {"name": "created by", "value": "pytan v3.0.0 on DATE"},
    {"name": "something", "value": "new", "show_console": False, "overwrite": True},
    {"name": "foo", "value": "bar"},
]
user = handler.mod_user_props("vittles7", props=props)

# create a user, provide 1 valid role name and 1 invalid role name
# user will be created, but without any roles
roles = [
    "Content Administrator",
    "No Such Roller, baller",
]
user = handler.create_user("vittles8", roles=roles)
print(user.hasroles._info())
print(user.notroles._info())

# modify a users roles, adding 3 roles
roles = ["Discover User", "Content Administrator", "Administrator"]
user = handler.mod_user_roles("vittles8", add_roles=roles)

# modify a users roles, removing all roles
user = handler.mod_user_roles("vittles8", del_all_roles=True)

# modify a users roles, adding 1 new one
roles = ["Discover User"]
user = handler.mod_user_roles("vittles8", add_roles=roles)

# modify a users roles, adding one that user already has
roles = ["Discover User"]
user = handler.mod_user_roles("vittles8", add_roles=roles)

# modify a users roles, removing one that user already has
roles = ["Discover User"]
user = handler.mod_user_roles("vittles8", del_roles=roles)

# modify a users roles, removing one that user does not have
roles = ["Discover User"]
user = handler.mod_user_roles("vittles8", del_roles=roles)

# get rid of all the test users
test_users = [x for x in handler.get_all("user") if x.name.startswith("vittles")]
[handler.session.delete(x) for x in test_users]
