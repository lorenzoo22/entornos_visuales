
CREATE TABLE users IF NOT EXISTS(id SERIAL PRIMARY KEY, nombre TEXT,apellido TEXT,nft TEXT ,riesgo TEXT);

INSERT INTO users(nombre,apellido,nft,riesgo) VALUES
    ('pepito', 'perez','mono_con_gafas_de_sol','alto');

INSERT INTO users(nombre,apellido,nft,riesgo) VALUES
    ('manolo', 'bombo','escudo_de_españa','bajo');

DROP TABLE users()

SELECT * FROM users;