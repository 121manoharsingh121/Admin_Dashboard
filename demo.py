# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DocverifyChoiceDealingAssistant(models.Model):
    id = models.BigAutoField(primary_key=True)
    dealing_assistant = models.CharField(max_length=100)
    duid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DocVerify_choice_dealing_assistant'


class DocverifyChoiceVerificationAssistant(models.Model):
    id = models.BigAutoField(primary_key=True)
    verification_assistant = models.CharField(max_length=100)
    vuid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DocVerify_choice_verification_assistant'


class DocverifyMigrationverification(models.Model):
    id = models.BigAutoField(primary_key=True)
    inst_code = models.CharField(max_length=255)
    inst_name = models.CharField(max_length=255)
    prog_code = models.CharField(max_length=255)
    prog_name = models.CharField(max_length=255)
    session = models.CharField(max_length=2)
    registration_number = models.BigIntegerField()
    roll_number = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255)
    dob = models.CharField(max_length=10)
    mobile_number = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    mother_name = models.CharField(max_length=255, blank=True, null=True)
    printing_date = models.CharField(max_length=10, blank=True, null=True)
    certificate_no = models.CharField(max_length=20, blank=True, null=True)
    is_duplicate = models.IntegerField()
    is_duplicate_issued = models.IntegerField()
    is_factory_print = models.IntegerField()
    semester = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DocVerify_migrationverification'


class DocverifyVerificationdispatchdetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_created = models.DateTimeField()
    dispatch_reference_no = models.CharField(unique=True, max_length=100)
    dispatch_dept = models.CharField(max_length=250)
    dispatch_date = models.DateField()
    remark = models.CharField(max_length=250, blank=True, null=True)
    verificationdocument_id_id = models.BigIntegerField(db_column='VerificationDocument_id_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DocVerify_verificationdispatchdetails'


class DocverifyVerificationdocumentdetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_created = models.DateTimeField()
    recieved_reference_no = models.CharField(unique=True, max_length=100)
    received_date = models.DateField()
    received_dept = models.CharField(max_length=250)
    doc_no_received_choice = models.CharField(max_length=20)
    doc_no_received = models.IntegerField()
    status = models.IntegerField()
    dispatchstatus = models.IntegerField()
    dealing_assistant_choice_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'DocVerify_verificationdocumentdetails'


class DocverifyVerificationperformed(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_created = models.DateTimeField()
    unpacked_rn = models.CharField(max_length=250)
    remark = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField()
    verificationdocument_id_id = models.BigIntegerField(db_column='VerificationDocument_id_id')  # Field name made lowercase.
    verification_assistant_choice_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DocVerify_verificationperformed'


class LoginDocvuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=254)
    name = models.CharField(max_length=254, blank=True, null=True)
    password = models.CharField(max_length=254, blank=True, null=True)
    user_type = models.PositiveSmallIntegerField()
    is_active = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Login_docvuser'


class PaymentReturnencdata(models.Model):
    encid = models.AutoField(db_column='encID', primary_key=True)  # Field name made lowercase.
    merchantordernumber = models.CharField(db_column='MerchantOrderNumber', unique=True, max_length=45)  # Field name made lowercase.
    sbiepayrefid = models.CharField(db_column='SBIePayRefID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transactionstatus = models.CharField(db_column='TransactionStatus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    paidamount = models.CharField(db_column='PaidAmount', max_length=45, blank=True, null=True)  # Field name made lowercase.
    merchantcurrency = models.CharField(db_column='MerchantCurrency', max_length=45, blank=True, null=True)  # Field name made lowercase.
    paymode = models.CharField(db_column='Paymode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    otherdetails = models.CharField(db_column='OtherDetails', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reason_message = models.CharField(db_column='Reason_Message', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bank_code = models.CharField(db_column='Bank_Code', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bank_reference_number = models.CharField(db_column='Bank_Reference_Number', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transaction_date = models.CharField(db_column='Transaction_Date', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transaction_country = models.CharField(db_column='Transaction_Country', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cin = models.CharField(db_column='CIN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    merchantid = models.CharField(db_column='MerchantID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    total_fee_gst = models.CharField(db_column='Total_Fee_GST', max_length=45, blank=True, null=True)  # Field name made lowercase.
    operatingmode = models.CharField(db_column='OperatingMode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    merchantcountry = models.CharField(db_column='MerchantCountry', max_length=45, blank=True, null=True)  # Field name made lowercase.
    aggregatorid = models.CharField(db_column='AggregatorID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    merchantcustomerid = models.CharField(db_column='MerchantCustomerID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    accessmedium = models.CharField(db_column='AccessMedium', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transactionsource = models.CharField(db_column='TransactionSource', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref1 = models.CharField(db_column='Ref1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref2 = models.CharField(db_column='Ref2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref3 = models.CharField(db_column='Ref3', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref4 = models.CharField(db_column='Ref4', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref5 = models.CharField(db_column='Ref5', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref6 = models.CharField(db_column='Ref6', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref7 = models.CharField(db_column='Ref7', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref8 = models.CharField(db_column='Ref8', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref9 = models.CharField(db_column='Ref9', max_length=45, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=45, blank=True, null=True)  # Field name made lowercase.
    examname = models.CharField(db_column='ExamName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    examheldin = models.CharField(db_column='ExamHeldIn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paymenttype = models.CharField(db_column='PaymentType', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payment_ReturnEncData'


class AcademicSession(models.Model):
    id = models.BigAutoField(primary_key=True)
    for_le = models.IntegerField(blank=True, null=True)
    is_current = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academic_session'


class Adminhod(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'adminhod'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class Bcece(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.TextField()  # This field type is a guess.
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255)
    category_admission = models.CharField(max_length=255)
    dob = models.DateField()
    father_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    is_le = models.TextField()  # This field type is a guess.
    is_reg = models.TextField()  # This field type is a guess.
    reg_no = models.BigIntegerField()
    roll_number = models.BigIntegerField()
    student = models.BigIntegerField(blank=True, null=True)
    student_name = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    institute = models.ForeignKey('Institute', models.DO_NOTHING, db_column='institute')
    program = models.ForeignKey('Program', models.DO_NOTHING, db_column='program')
    remarks2 = models.CharField(max_length=255, blank=True, null=True)
    regamount = models.CharField(db_column='regAmount', max_length=4, blank=True, null=True)  # Field name made lowercase.
    isregamountpaid = models.TextField(db_column='isregAmountPaid', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    feepaiddatetime = models.CharField(max_length=50, blank=True, null=True)
    atrano_sbi = models.CharField(db_column='ATRANO_SBI', max_length=45, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(max_length=150, blank=True, null=True)
    mobileno = models.CharField(db_column='Mobileno', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bcece'


class CertificateVerification(models.Model):
    id = models.BigIntegerField()
    inst_code = models.CharField(max_length=255, db_collation='utf8_general_ci')
    inst_name = models.CharField(max_length=255, db_collation='utf8_general_ci')
    prog_code = models.CharField(max_length=255, db_collation='utf8_general_ci')
    prog_name = models.CharField(max_length=255, db_collation='utf8_general_ci')
    session = models.CharField(max_length=2)
    registration_number = models.BigIntegerField()
    roll_number = models.CharField(max_length=255, db_collation='utf8_general_ci')
    aadhar_number = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    first_name = models.CharField(max_length=255, db_collation='utf8_general_ci')
    middle_name = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    last_name = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    sex = models.CharField(max_length=255, db_collation='utf8_general_ci')
    dob = models.CharField(max_length=10)
    category = models.CharField(max_length=255, db_collation='utf8_general_ci')
    mobile_number = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    father_name = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    mother_name = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    exam_held_year = models.CharField(max_length=4)
    exam_held_month = models.CharField(max_length=2)
    result = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    printing_date = models.CharField(max_length=10, blank=True, null=True)
    certificate_no = models.CharField(max_length=20, blank=True, null=True)
    is_duplicate = models.IntegerField()
    is_duplicate_issued = models.IntegerField()
    is_factory_print = models.IntegerField()
    obtained_marks = models.IntegerField()
    max_marks_upto_6th = models.BigIntegerField()
    number_40_per_marks = models.IntegerField(db_column='40_per_marks')  # Field renamed because it wasn't a valid Python identifier.
    obtained_marks_upto_6th = models.BigIntegerField()
    cgpa = models.FloatField(blank=True, null=True)
    sgpa = models.FloatField()

    class Meta:
        managed = False
        db_table = 'certificate_verification'


class CourseLe(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    full_mark = models.IntegerField()
    is_deleted = models.TextField()  # This field type is a guess.
    name = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'course_le'


class CourseRegistrationOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    code = models.CharField(max_length=255)
    is_deleted = models.IntegerField()
    name = models.CharField(max_length=255)
    registration_old_id = models.BigIntegerField()
    type = models.CharField(max_length=255)
    is_scrutiny = models.IntegerField()
    is_verified = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'course_registration_old'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoDbLoggerStatuslog(models.Model):
    logger_name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField()
    msg = models.TextField()
    trace = models.TextField(blank=True, null=True)
    create_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_db_logger_statuslog'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmsappEvent(models.Model):
    eventid = models.AutoField(primary_key=True)
    eventname = models.CharField(db_column='EventName', max_length=255)  # Field name made lowercase.
    eventmessage = models.CharField(db_column='EventMessage', max_length=255)  # Field name made lowercase.
    eventstartdatetime = models.DateTimeField(db_column='EventStartDateTime')  # Field name made lowercase.
    eventenddatetime = models.DateTimeField(db_column='EventEndDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emsapp_event'


class Exams(models.Model):
    id = models.BigAutoField(primary_key=True)
    academic_term = models.CharField(max_length=255)
    exam_held = models.CharField(max_length=255, blank=True, null=True)
    is_current = models.IntegerField(blank=True, null=True)
    term = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exams'


class FeeStructure(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_over = models.DateTimeField()
    due_date = models.DateTimeField()
    fee = models.DecimalField(max_digits=7, decimal_places=2)
    fee_type = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.TextField()  # This field type is a guess.
    late_fee = models.DecimalField(max_digits=7, decimal_places=2)
    max_fee = models.DecimalField(max_digits=7, decimal_places=2)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    term = models.IntegerField()
    academic_term = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fee_structure'


class FilePath(models.Model):
    id = models.BigAutoField(primary_key=True)
    path = models.CharField(max_length=255)
    row_page = models.IntegerField()
    type = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'file_path'


class Institute(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    is_deleted = models.IntegerField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_marksentry = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'institute'


class LastAcademicRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.TextField()  # This field type is a guess.
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    board_name = models.CharField(max_length=255)
    exam_name = models.CharField(max_length=255)
    exam_type = models.CharField(max_length=255)
    institute_name = models.CharField(max_length=255)
    passing_year = models.CharField(max_length=4)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    result = models.CharField(max_length=255)
    roll_number = models.CharField(max_length=255)
    subjects = models.CharField(max_length=255)
    student = models.ForeignKey('Student', models.DO_NOTHING, db_column='student')

    class Meta:
        managed = False
        db_table = 'last_academic_record'


class MarksheetVerification(models.Model):
    id = models.BigIntegerField()
    inst_code = models.CharField(max_length=255, db_collation='utf8_general_ci')
    inst_name = models.CharField(max_length=255, db_collation='utf8_general_ci')
    prog_code = models.CharField(max_length=255, db_collation='utf8_general_ci')
    prog_name = models.CharField(max_length=255, db_collation='utf8_general_ci')
    session = models.CharField(max_length=2)
    registration_number = models.BigIntegerField()
    roll_number = models.CharField(max_length=255, db_collation='utf8_general_ci')
    aadhar_number = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    first_name = models.CharField(max_length=255, db_collation='utf8_general_ci')
    middle_name = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    last_name = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    sex = models.CharField(max_length=255, db_collation='utf8_general_ci')
    dob = models.CharField(max_length=10)
    category = models.CharField(max_length=255, db_collation='utf8_general_ci')
    mobile_number = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    father_name = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    mother_name = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    exam_held_year = models.CharField(max_length=4)
    exam_held_month = models.CharField(max_length=2)
    result = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    printing_date = models.CharField(max_length=10, blank=True, null=True)
    marksheet_no = models.BigIntegerField()
    is_duplicate = models.IntegerField()
    is_duplicate_issued = models.IntegerField()
    obtained_marks = models.IntegerField()
    max_marks_upto_6th = models.BigIntegerField()
    number_40_per_marks = models.IntegerField(db_column='40_per_marks')  # Field renamed because it wasn't a valid Python identifier.
    obtained_marks_upto_6th = models.BigIntegerField()
    cgpa = models.FloatField(blank=True, null=True)
    sgpa = models.FloatField()
    semester = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marksheet_verification'


class OldMarks(models.Model):
    id = models.BigIntegerField()
    version = models.BigIntegerField()
    is_absent = models.IntegerField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    marks1 = models.IntegerField(blank=True, null=True)
    marks2 = models.IntegerField(blank=True, null=True)
    marks_obtained = models.IntegerField(blank=True, null=True)
    old_task_id = models.BigIntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)
    roll_number = models.CharField(max_length=20)
    student_id = models.BigIntegerField()
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    is_absent1 = models.IntegerField()
    is_absent2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'old_marks'


class OldTask(models.Model):
    id = models.BigIntegerField()
    version = models.BigIntegerField()
    academic_term = models.CharField(max_length=255)
    compiler_id = models.BigIntegerField(blank=True, null=True)
    course_title = models.CharField(max_length=255)
    institute_id = models.BigIntegerField()
    is_compiled = models.IntegerField()
    is_deleted = models.TextField()  # This field type is a guess.
    is_finalized = models.IntegerField()
    is_opr1finalized = models.IntegerField()
    is_opr2finalized = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    max_marks = models.IntegerField()
    operator1_id = models.BigIntegerField(blank=True, null=True)
    operator2_id = models.BigIntegerField(blank=True, null=True)
    program_id = models.BigIntegerField()
    student_count = models.IntegerField()
    term = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'old_task'


class PaymentReturnencsuccess(models.Model):
    encid = models.AutoField(db_column='encID', primary_key=True)  # Field name made lowercase.
    merchantordernumber = models.CharField(db_column='MerchantOrderNumber', unique=True, max_length=45)  # Field name made lowercase.
    sbiepayrefid = models.CharField(db_column='SBIePayRefID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transactionstatus = models.CharField(db_column='TransactionStatus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    paidamount = models.CharField(db_column='PaidAmount', max_length=45, blank=True, null=True)  # Field name made lowercase.
    merchantcurrency = models.CharField(db_column='MerchantCurrency', max_length=45, blank=True, null=True)  # Field name made lowercase.
    paymode = models.CharField(db_column='Paymode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    otherdetails = models.CharField(db_column='OtherDetails', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reason_message = models.CharField(db_column='Reason_Message', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bank_code = models.CharField(db_column='Bank_Code', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bank_reference_number = models.CharField(db_column='Bank_Reference_Number', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transaction_date = models.CharField(db_column='Transaction_Date', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transaction_country = models.CharField(db_column='Transaction_Country', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cin = models.CharField(db_column='CIN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    merchantid = models.CharField(db_column='MerchantID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    total_fee_gst = models.CharField(db_column='Total_Fee_GST', max_length=45, blank=True, null=True)  # Field name made lowercase.
    operatingmode = models.CharField(db_column='OperatingMode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    merchantcountry = models.CharField(db_column='MerchantCountry', max_length=45, blank=True, null=True)  # Field name made lowercase.
    aggregatorid = models.CharField(db_column='AggregatorID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    merchantcustomerid = models.CharField(db_column='MerchantCustomerID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    accessmedium = models.CharField(db_column='AccessMedium', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transactionsource = models.CharField(db_column='TransactionSource', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref1 = models.CharField(db_column='Ref1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref2 = models.CharField(db_column='Ref2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref3 = models.CharField(db_column='Ref3', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref4 = models.CharField(db_column='Ref4', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref5 = models.CharField(db_column='Ref5', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref6 = models.CharField(db_column='Ref6', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref7 = models.CharField(db_column='Ref7', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref8 = models.CharField(db_column='Ref8', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ref9 = models.CharField(db_column='Ref9', max_length=45, blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=45, blank=True, null=True)  # Field name made lowercase.
    examname = models.CharField(db_column='ExamName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    examheldin = models.CharField(db_column='ExamHeldIn', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paymenttype = models.CharField(db_column='PaymentType', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment_returnencsuccess'


class Paymentordertbl(models.Model):
    studentid = models.BigIntegerField()
    order_number = models.CharField(db_column='Order_Number', max_length=50)  # Field name made lowercase.
    rollno = models.CharField(db_column='RollNo', max_length=50)  # Field name made lowercase.
    payamount = models.CharField(db_column='PayAmount', max_length=10)  # Field name made lowercase.
    ordercreationdate = models.CharField(db_column='OrderCreationDate', max_length=50)  # Field name made lowercase.
    examname = models.CharField(db_column='ExamName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    examheldin = models.CharField(db_column='ExamHeldin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paymenttype = models.CharField(db_column='PaymentType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paymentstatus = models.CharField(db_column='PaymentStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tran_datetime = models.CharField(db_column='Tran_datetime', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paymentordertbl'
        unique_together = (('id', 'studentid', 'order_number'), ('studentid', 'order_number'),)


class Program(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    is_deleted = models.IntegerField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'program'


class RegistrationOld(models.Model):
    id = models.BigIntegerField()
    version = models.BigIntegerField()
    academic_term = models.CharField(max_length=255)
    form_amount = models.FloatField(blank=True, null=True)
    form_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    is_form_filled = models.IntegerField()
    is_form_verified = models.IntegerField()
    is_online_form_filled = models.IntegerField()
    is_repeat_registration = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    registration_code = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    roll_number = models.CharField(max_length=255)
    student_id = models.BigIntegerField()
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    valid_till = models.DateTimeField(blank=True, null=True)
    scrutiny_amount = models.FloatField(blank=True, null=True)
    scrutiny_date = models.DateTimeField(blank=True, null=True)
    scrutiny_verified_date = models.DateTimeField(blank=True, null=True)
    is_scrutiny_verified = models.IntegerField()
    is_individual = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registration_old'


class RegistrationScrutiny(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.TextField()  # This field type is a guess.
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    academic_term = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    scrutiny = models.IntegerField()
    verified = models.TextField()  # This field type is a guess.
    roll_number = models.CharField(max_length=255)
    scrutiny_date = models.DateTimeField(blank=True, null=True)
    valid_till = models.DateTimeField(blank=True, null=True)
    verified_date = models.DateTimeField(blank=True, null=True)
    student = models.ForeignKey('Student', models.DO_NOTHING, db_column='student')
    payment_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registration_scrutiny'


class ReportSample(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    phonenumb = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'report_sample'


class RoleView(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.TextField()  # This field type is a guess.
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'role_view'


class ScrutinyCourse(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.TextField()  # This field type is a guess.
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255)
    scrutiny = models.IntegerField()
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    reg = models.ForeignKey(RegistrationScrutiny, models.DO_NOTHING, db_column='reg')

    class Meta:
        managed = False
        db_table = 'scrutiny_course'


class SeatApproval(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.TextField()  # This field type is a guess.
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    approved_filled = models.BigIntegerField(blank=True, null=True)
    approved_seat = models.BigIntegerField(blank=True, null=True)
    handicapped_filled = models.BigIntegerField(blank=True, null=True)
    handicapped_seat = models.BigIntegerField(blank=True, null=True)
    institute = models.BigIntegerField(blank=True, null=True)
    le_filled = models.BigIntegerField(blank=True, null=True)
    le_seat = models.BigIntegerField(blank=True, null=True)
    program = models.BigIntegerField(blank=True, null=True)
    waiver_scheme_filled = models.BigIntegerField(blank=True, null=True)
    waiver_scheme_seat = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seat_approval'


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    aadhar_number = models.CharField(max_length=255, blank=True, null=True)
    admission_type = models.CharField(max_length=255, blank=True, null=True)
    bcece = models.BigIntegerField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    category_admission = models.CharField(max_length=255, blank=True, null=True)
    class_roll_no = models.BigIntegerField(blank=True, null=True)
    comm_city = models.CharField(max_length=255, blank=True, null=True)
    comm_country = models.CharField(max_length=255, blank=True, null=True)
    comm_line1 = models.CharField(max_length=255, blank=True, null=True)
    comm_line2 = models.CharField(max_length=255, blank=True, null=True)
    comm_pin = models.CharField(max_length=6, blank=True, null=True)
    comm_state = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField()
    doj = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    is_iti = models.IntegerField(blank=True, null=True)
    is_rec = models.TextField()  # This field type is a guess.
    last_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    mobile_no = models.CharField(max_length=255, blank=True, null=True)
    mother_name = models.CharField(max_length=255, blank=True, null=True)
    perm_city = models.CharField(max_length=255, blank=True, null=True)
    perm_country = models.CharField(max_length=255, blank=True, null=True)
    perm_line1 = models.CharField(max_length=255, blank=True, null=True)
    perm_line2 = models.CharField(max_length=255, blank=True, null=True)
    perm_pin = models.CharField(max_length=6, blank=True, null=True)
    perm_state = models.CharField(max_length=255, blank=True, null=True)
    reg_amount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    reg_no = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    student_name = models.CharField(max_length=255, blank=True, null=True)
    academic_session = models.BigIntegerField(blank=True, null=True)
    institute = models.BigIntegerField()
    program = models.BigIntegerField()
    is_issued = models.IntegerField(blank=True, null=True)
    is_provisional = models.IntegerField(blank=True, null=True)
    is_registered = models.IntegerField(blank=True, null=True)
    is_new = models.IntegerField(blank=True, null=True)
    bcece_roll_no = models.BigIntegerField(blank=True, null=True)
    paymentstatus = models.IntegerField(db_column='PaymentStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    is_superuser = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    user_type = models.CharField(max_length=2)
    email = models.CharField(unique=True, max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_admin = models.IntegerField()
    reg_date_time = models.DateTimeField()
    date_joined = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    modified_by = models.CharField(max_length=255, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    is_passupdated = models.IntegerField(blank=True, null=True)
    institute = models.ForeignKey(Institute, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_groups'
        unique_together = (('user', 'group'),)


class UserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_permissions'
        unique_together = (('user', 'permission'),)
