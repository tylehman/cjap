def decide_on_model(model):
    """Small helper formula to pipe all DB operations of a jobs model to the jobs_data DB"""
    return 'jobs_data' if model._meta.app_label == 'jobs' else None

class JobsDbRouter:

    def db_for_read(self, model, **hints):
        return decide_on_model(model)

    def db_for_write(self, model, **hints):
        return decide_on_model(model)

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'jobs' and obj2._meta.app_level == 'jobs':
            return True
        elif 'jobs' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'default' and app_label != 'jobs':
            return True

        if db == 'jobs_data' and app_label == 'jobs':
            return True

        return False
