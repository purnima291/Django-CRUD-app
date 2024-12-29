class LegacyDBRouter:
    """
    A database router to control all database opertaions on models in the stock market analytics application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to Stock models go to legacy DB.
        """
        if model._meta.db_table == 'stocks':
            return 'legacy'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write Stocks models go to legacy DB.
        """
        if model._meta.db_table == 'stocks':
            return 'legacy'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both objects are in the same database.
        """
        # If both the object are stock related, allow the relation
        if obj1._meta.db_table == 'stocks' and obj2._meta.db_table == 'stocks':
            return True
        # If nether object is stock related, allow the relation
        elif 'stocks' not in (obj1._meta.db_table, obj2._meta.db_table):
            return True
        return False
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        To make sure the stock models only appear in 'legacy' database.
        """
        if model_name == 'stocks':
            return db == 'legacy'
        return db == 'default'