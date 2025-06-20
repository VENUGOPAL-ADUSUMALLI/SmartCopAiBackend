from django.db import models
import uuid



class User(models.Model):
    USER_ROLES = (
        ('citizen', 'Citizen'),
        ('officer', 'Officer'),
        ('admin', 'Admin'),
    )

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)
    permanent_address = models.TextField()
    current_address = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='citizen')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class CaseType(models.Model):
    CASE_TYPE_CHOICES = (
        ('murder', 'Murder'),
        ('theft', 'Theft'),
        ('crime_against_women', 'Crime Against Women'),
        ('public_nuisance', 'Public Nuisance'),
    )

    case_type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, choices=CASE_TYPE_CHOICES, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.get_name_display()


class Complaint(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('under_review', 'Under Review'),
        ('resolved', 'Resolved'),
    )

    complaint_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    
    case_type = models.ForeignKey(CaseType, on_delete=models.PROTECT)

    incident_date = models.DateField()
    incident_time = models.TimeField()
    location = models.TextField()
    incident_summary = models.TextField()
    ai_urgency_score = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.case_type} - {self.user.name}"



class Evidence(models.Model):
    EVIDENCE_TYPE = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('document', 'Document'),
    )

    evidence_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, related_name='evidence')
    file_url = models.TextField()
    type = models.CharField(max_length=10, choices=EVIDENCE_TYPE)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Accused(models.Model):
    accused_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, related_name='accused')
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)



class Witness(models.Model):
    witness_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, related_name='witnesses')
    name = models.CharField(max_length=100)
    contact_info = models.TextField(blank=True, null=True)
    statement = models.TextField(blank=True, null=True)



class AIAssessment(models.Model):
    assessment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    complaint = models.OneToOneField(Complaint, on_delete=models.CASCADE, related_name='assessment')
    ipc_sections = models.JSONField()  
    ipc_descriptions = models.JSONField()  
    urgency_score = models.IntegerField(default=0)
    model_version = models.CharField(max_length=50)
    generated_at = models.DateTimeField(auto_now_add=True)


class ChatQuery(models.Model):
    MODE_CHOICES = (
        ('voice', 'Voice'),
        ('text', 'Text'),
    )

    query_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query_text = models.TextField()
    response_text = models.TextField()
    language = models.CharField(max_length=50)
    mode = models.CharField(max_length=10, choices=MODE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
