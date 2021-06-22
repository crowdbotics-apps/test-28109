
def make_fields_permissions(Permission, ContentType, Model):
    mode_name = Model.__name__.lower()
    permissions = []
    for item in Model._meta.fields:
        permissions.append(('view_' + mode_name + '.' + item.name + '_field',
                            'Can view ' + item.name.replace('_', ' ')))

    for item in Model._meta.fields:
        permissions.append(('change_' + mode_name + '.' + item.name + '_field',
                            'Can change ' + item.name.replace('_', ' ')))
    for codename, permission_name in permissions:
        Permission.objects.get_or_create(
            codename=codename,
            name=permission_name,
            content_type=ContentType.objects.get_for_model(Model),
        )

