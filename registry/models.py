from django.db import models

# Đơn Vị hành chính cũ
class ProvinceOld(models.Model):
    TYPE_CHOICES = (
    ("Tỉnh", "Tỉnh"),
    ("Thành Phố", "Thành Phố"),
)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="Tỉnh")

    def __str__(self):
        return f"{self.type} {self.name}"

class District(models.Model):
    TYPE_CHOICES = (
    ("Huyện", "Huyện"),
    ("Thành Phố", "Thành Phố"),
    ("Thị Xã", "Thị Xã"),
    ("Quận", "Quận"),
)
    name = models.CharField(max_length=100)
    province = models.ForeignKey(ProvinceOld, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="Huyện")
    
    def __str__(self):
        return f"{self.name} - {self.province.name}"

class CommuneOld(models.Model):
    TYPE_CHOICES = (
    ("Xã", "Xã"),
    ("Phường", "Phường"),
    ("Thị Trấn", "Thị Trấn"),
)
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="Xã")
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    # province = models.ForeignKey(ProvinceOld, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.district.name} - {self.district.province.name}"


# Đơn Vị hành chính mới
class ProvinceNew(models.Model):
    TYPE_CHOICES = (
    ("Tỉnh", "Tỉnh"),
    ("Thành Phố", "Thành Phố"),
)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="Tỉnh")

    def __str__(self):
        return f"{self.type} {self.name}"
    
class CommuneNew(models.Model):
    TYPE_CHOICES = (
    ("Xã", "Xã"),
    ("Phường", "Phường"),
    ("Thị Trấn", "Thị Trấn"),
)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="Xã")
    province = models.ForeignKey(ProvinceNew, on_delete=models.CASCADE)
    class Meta:
        unique_together = ("name", "province")  # mỗi tỉnh có thể có xã trùng tên, nhưng trong cùng 1 tỉnh thì không
    
    def __str__(self):
        return f"{self.name} - {self.province.name}"
    
    
# Bảng lưu trữ lịch sử thay đổi đơn vị hành chính
class CommuneHistory(models.Model):
    commune_old = models.ForeignKey(CommuneOld, on_delete=models.CASCADE)
    commune_new = models.ForeignKey(CommuneNew, on_delete=models.CASCADE)
    change_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.commune_old.name} xác nhập vào {self.commune_new.name} vào ngày {self.change_date}"
    