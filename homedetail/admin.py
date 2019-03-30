from django.contrib import admin

# Register your models here.

from homedetail.models import Room, DataType, Data


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('RoomNumber', 'RoomDetail', 'UserID', 'status')


@admin.register(DataType)
class DataTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'DataType_Name', 'DataTypeDetail', 'Rate')
    list_editable = ['Rate']


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'RoomId', 'Data_Type', 'DataDate', 'DataDeadLine', 'Detail', 'status', )
    list_filter = ('Data_Type', 'DataDate', 'RoomId')

