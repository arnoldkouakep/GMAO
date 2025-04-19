def set_permission(connection, module_name, role, can_access):
    with connection:
        connection.execute(
            """
            INSERT INTO permissions (module_name, role, can_access)
            VALUES (?, ?, ?)
            ON CONFLICT(module_name, role) DO UPDATE SET can_access = ?
            """,
            (module_name, role, can_access, can_access),
        )

def check_permission(connection, module_name, role):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT can_access FROM permissions WHERE module_name = ? AND role = ?",
        (module_name, role),
    )
    result = cursor.fetchone()
    return result[0] == 1 if result else False
