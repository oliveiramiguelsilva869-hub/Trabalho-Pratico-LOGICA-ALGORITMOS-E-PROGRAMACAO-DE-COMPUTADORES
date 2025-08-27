def loginUsuario(perfil):
  if perfil.lower() == 'admin':
    print('Bem-vindo, Administrador')
  else:
    print('Bem-vindo, Usuário')

print("Teste com 'Admin':")
loginUsuario('Admin')

print("\nTeste com 'admin':")
loginUsuario('admin')

print("\nTeste com 'User':")
loginUsuario('User')

print("\nTeste com 'usuário':")
loginUsuario('usuário')
