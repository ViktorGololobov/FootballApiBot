from peewee import Model, SqliteDatabase, ForeignKeyField, CharField, BigIntegerField, DateField, AutoField


DB_PATH = SqliteDatabase('database.db')

DATE_FORMAT = "%d.%m.%Y"


class BaseModel(Model):
    """ Модель общей БД. """

    class Meta:
        database = DB_PATH


class Users(BaseModel):
    """ Модель пользователя. """

    user_id = BigIntegerField(primary_key=True)
    username = CharField(null=True)
    first_name = CharField(null=True)
    last_name = CharField(null=True)


class Task(BaseModel):
    """
    Модель запроса.

    Methods:
    ----------
    str()
        Возвращает строку с запросом.
    """
    task_id = AutoField()
    user_id = ForeignKeyField(Users, backref="tasks")
    message_text = CharField()
    due_date = DateField()

    def __str__(self):
        return "Id пользователя: {user_id}, запрос: {message_text}, дата запроса: {due_date}".format(
            user_id=self.user_id,
            message_text=self.message_text,
            due_date=self.due_date,
        )


def create_models() -> None:
    """ Функция для создания БД. """

    DB_PATH.create_tables(BaseModel.__subclasses__())
