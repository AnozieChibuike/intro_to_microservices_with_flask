Because this is a shared db microservice, you want to adjust the migrations to incorporate the tables from other microservices

Go into <code>migration/env.py</code> and edit the two variables called <code>alembic_table_name</code> and <code>tables</code>.

Incase of fresh migration folder you can copy the current <code>migration/env.py</code> file and replace with the auto generated file by flask migrate incase you used it... the follow the above step