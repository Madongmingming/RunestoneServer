db.define_table('user_biography',
  Field('user_id', 'reference auth_user'),
  Field('prefered_name', 'string'),
  Field('pronounced_name', 'string'),
  Field('interesting_fact', 'string'),
  Field('programming_experience', 'string'),
  Field('laptop_type', 'string'),
  migrate='runestone_user_biography.table')
