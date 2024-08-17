-- Crear el usuario 'usuarioprincipal'
CREATE USER 'usuarioprincipal'@'localhost' IDENTIFIED BY '1';

-- Crear el usuario 'abogadoprincipal'
CREATE USER 'abogadoprincipal'@'localhost' IDENTIFIED BY '2';

-- Crear el usuario 'abogadosecundario'
CREATE USER 'abogadosecundario'@'localhost' IDENTIFIED BY '3';

-- Otorgar todos los privilegios en la base de datos EstudioJuridicoDB al usuario 'usuarioprincipal'
GRANT ALL PRIVILEGES ON EstudioJuridicoDB.* TO 'usuarioprincipal'@'localhost';

-- Otorgar el privilegio CREATE USER globalmente al usuario 'abogadoprincipal'
GRANT CREATE USER, EXECUTE ON *.* TO 'abogadoprincipal'@'localhost';

-- Otorgar el privilegio EXECUTE en la base de datos EstudioJuridicoDB al usuario 'abogadosecundario'
GRANT EXECUTE ON EstudioJuridicoDB.* TO 'abogadosecundario'@'localhost';

-- Aplicar los cambios
FLUSH PRIVILEGES;

SHOW GRANTS FOR 'abogadoprincipal'@'localhost';

