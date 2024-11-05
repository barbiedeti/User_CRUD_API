User CRUD API

Esta é uma **API REST** desenvolvida com **Flask** que permite a criação, leitura, atualização e exclusão de usuários (operações CRUD) em um banco de dados SQLite. A API fornece endpoints para gerenciar as informações dos usuários, incluindo nome e e-mail.

Tecnologias Utilizadas

	•	Python e Flask para desenvolvimento do servidor.
	•	Flask-RESTful para estruturação da API.
	•	Flask-SQLAlchemy para ORM e gerenciamento do banco de dados SQLite.

Funcionalidades

	•	Criação de Usuário: Cria um novo usuário com nome e e-mail exclusivos.
	•	Listagem de Usuários: Retorna todos os usuários cadastrados.
	•	Busca por Usuário: Retorna um usuário específico com base no ID.
	•	Atualização de Usuário: Permite a atualização parcial (patch) dos dados de um usuário.
	•	Exclusão de Usuário: Exclui um usuário com base no ID.

Dependências

	•	Flask
	•	Flask-RESTful
	•	Flask-SQLAlchemy

Instale todas as dependências com:

pip install Flask Flask-RESTful Flask-SQLAlchemy

Licença

Este projeto é de uso livre. Fique à vontade para utilizá-lo e adaptá-lo conforme necessário.
