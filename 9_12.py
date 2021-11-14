from Adminusers import Admin
from user import User, Privileges

giovanni = Admin('giovanni', 'pepi', 27, 'programming')
giovanni.show_privileges()

luke = User('luke', 'pepiprado', 1, 'meowing')
luke.describe_user()