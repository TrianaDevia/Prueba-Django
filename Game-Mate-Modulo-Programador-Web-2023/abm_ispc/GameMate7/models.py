from django.contrib.auth.models import AbstractUser, Group, Permission #PermissionsMixin, 
#from django.db.models.signals import post_save
#from django.contrib.auth.models import User, UserManager
from django.db import models
from django.utils import timezone





#from django.utils import timezone
#from django.db import models
#from django.contrib.auth.models import User 
#from django.db.models.signals import post_save
# Create your models here.

class CustomUser(AbstractUser):  
                #PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
     #['first_name','last_name']

    #def __str__(self):
        #return self.email
    

class Categoria(models.Model):
    id_categoria= models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=20, blank=False)
    informacion= models.CharField(max_length=100, blank=False)
    class Meta:
        db_table="categoria"
        verbose_name="categoria de productos"
        verbose_name_plural="categorias"
    def __unicode__ (self):
        return self.id_categoria
    def __str__ (self):
        return self.id_categoria

class Cliente(models.Model):
    id_cliente= models.AutoField(primary_key=True)
    nombre_completo= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    dni= models.IntegerField()
    telefono= models.BigIntegerField()
    nickname= models.CharField(max_length=15, null=True)
    class Meta:
        db_table="cliente"
        verbose_name="datos de los clientes"
        verbose_name_plural="clientes"
    def __unicode__ (self):
        return self.id_cliente
    def __str__ (self):
        return self.id_cliente
    
class Proveedor(models.Model):
    id_proveedor= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=50)
    telefono= models.CharField(max_length=20)
    cuil= models.CharField(max_length=15)
    email= models.EmailField()
    class Meta:
        db_table="Proveedor"
        verbose_name="datos del proveedor"
        verbose_name_plural="Proveedores"
    def __unicode__ (self):
        return self.id_proveedor
    def __str__ (self):
        return self.id_proveedor

class Direccion(models.Model):
    id_direccion= models.CharField(max_length=50, primary_key=True)
    direccion= models.CharField(max_length=30)
    cod_post= models.IntegerField()
    provincia= models.CharField(max_length=30)
    localidad= models.CharField(max_length=50)
    Proveedor= models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    class Meta:
        db_table="direccion"
        verbose_name="todas las direcciones"
        verbose_name_plural="direcciones"
    def __unicode__ (self):
        return self.id_direccion
    def __str__ (self):
        return self.id_direccion
    
class Usuarios(models.Model):
    user= models.CharField(primary_key=True, max_length=15)
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    fecha_nac= models.DateField()
    provincia= models.CharField(max_length=15)
    disp_horaria= models.CharField(max_length=6)
    email= models.CharField(max_length=25)
    contraseña= models.CharField(max_length=10)
    imagen_perfil= models.CharField(max_length=50, null=True)
    descripcion= models.CharField(max_length=255, null=True)
    class Meta:
        db_table="Usuarios"
        verbose_name="datos de los usuarios"
        verbose_name_plural="Usuarios"
    def __unicode__ (self):
        return self.user 
    def __str__ (self):
        return self.user.username
def create_user_usuarios(sender , instance , create,**kwargs ):
    if create:
        Usuarios.objects.create(user=instance)
def save_user_usuarios(sender , instance , **kwargs):
    instance.usuarios.save()

class Juegos(models.Model):
    id_juego = models.IntegerField(primary_key=True)
    juego = models.CharField(max_length=30)
    imagen = models.CharField(max_length=100)
    class Meta:
        db_table="Juegos"
        verbose_name="Juegos"
        verbose_name_plural="Juegos"
    def __unicode__ (self):
        return self.id_juego
    def __str__ (self):
        return self.id_juego

class Jugar(models.Model):
    nivel_jugador = models.CharField(max_length=15)
    Usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    Juegos = models.ForeignKey(Juegos, on_delete=models.CASCADE)
    class Meta:
        db_table="Jugar"
        verbose_name="Jugar"
        verbose_name_plural="Jugaremos"
    def __unicode__ (self):
        return self.nivel_jugador
    def __str__ (self):
        return self.nivel_jugador
    
class Dispositivos(models.Model):
    id_dispositivos= models.IntegerField(primary_key=True)
    pc = models.CharField(max_length=15, null=True)
    version_celular= models.CharField(max_length=15, null=True)
    nintendo_switch= models.CharField(max_length=10, null=True)
    version_playstation= models.CharField(max_length=10, null=True)
    version_xbox= models.CharField(max_length=10, null=True)
    Usuarios= models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    class Meta:
        db_table="dispositivos"
        verbose_name="dispositivos"
        verbose_name_plural="dispositivos"
    def __unicode__ (self):
        return self.id_dispositivos
    def __str__ (self):
        return self.id_dispositivos
    

class Compatibilidad(models.Model):
    Juegos= models.ForeignKey(Juegos, on_delete=models.CASCADE)
    Dispositivos= models.ForeignKey(Dispositivos, on_delete=models.CASCADE)
    class Meta:
        db_table="compatibilidad"
        verbose_name="compatibilidad"
        verbose_name_plural="compatibilidades"
    def __unicode__ (self):
        return self.nombre
    def __str__ (self):
        return self.nombre
    
    
class Envio(models.Model):
    id_envio= models.IntegerField(primary_key=True)
    fecha_envio= models.DateField()
    localidad= models.CharField(max_length=20)
    provincia= models.CharField(max_length=20)
    cod_post= models.IntegerField()
    estado_envio= models.CharField(max_length=20)
    direccion_envio= models.CharField(max_length=30)
    metodo_envio= models.CharField(max_length=30)
    Cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    class Meta:
        db_table="envio"
        verbose_name="informacion de envio"
        verbose_name_plural="envios"
    def __unicode__ (self):
        return self.id_envio
    def __str__ (self):
        return self.id_envio
    
class Orden(models.Model):
    id_orden= models.AutoField(primary_key=True)
    fecha= models.DateField()
    monto_total= models.DecimalField(max_digits=6, decimal_places=2)
    precio_unitario= models.DecimalField(max_digits=5, decimal_places=2)
    cantidad_pedido= models.IntegerField()
    Cliente= models.ForeignKey('Cliente', on_delete=models.CASCADE)
    Producto= models.ForeignKey('Producto', on_delete=models.CASCADE)
    class Meta:
        db_table="Orden"
        verbose_name="datos de la orden"
        verbose_name_plural="Ordenes"
    def __unicode__ (self):
        return self.id_orden 
    def __str__ (self):
        return self.id_orden 
    
class Facturacion(models.Model):
    numero_factura= models.IntegerField(primary_key=True)
    metodo_pago= models.CharField(max_length=20)
    costo_envio= models.DecimalField(max_digits=5, decimal_places=2, null=True)
    fecha_factura= models.DateField()
    fecha_pago= models.DateField()
    monto_total= models.DecimalField(max_digits=6, decimal_places=2)
    estado_pago= models.CharField(max_length=20, null=True)
    Orden= models.ForeignKey (Orden, on_delete=models.CASCADE)
    class Meta:
        db_table="Facturacion"
        verbose_name="informacion de Facturacion"
        verbose_name_plural="Facturaciones"
    def __unicode__ (self):
        return self.numero_factura
    def __str__ (self):
        return self.numero_factura

class Galeria(models.Model):
    id_galeria= models.IntegerField(primary_key=True)
    nombre_foto= models.CharField(max_length=25, null=True)
    foto= models.CharField(max_length=50, null=True)
    jugador= models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    class Meta:
        db_table="Galeria"
        verbose_name="galeria de fotos"
        verbose_name_plural="Galerias"
    def __unicode__ (self):
        return self.id_galeria
    def __str__ (self):
        return self.id_galeria
    
    
class Pedido(models.Model):
    id_pedido= models.AutoField(primary_key=True)
    fecha_pedido= models.DateField()
    estado_pedido= models.CharField(max_length=20)
    Envio= models.ForeignKey('Envio', on_delete=models.CASCADE)
    Cliente= models.ForeignKey('Cliente', on_delete=models.CASCADE)
    Facturacion= models.ForeignKey('Facturacion', on_delete=models.CASCADE)
    class Meta:
        db_table="Pedido"
        verbose_name="datos del pedido"
        verbose_name_plural="Pedidos"
    def __unicode__ (self):
        return self.id_pedido
    def __str__ (self):
        return self.id_pedido

class Producto(models.Model):
    id_producto= models.AutoField(primary_key=True)
    precio= models.DecimalField(max_digits=5, decimal_places=2)
    stock= models.IntegerField()
    nombre= models.CharField(max_length=30)
    descripcion= models.CharField(max_length=100, null=True, blank=True)
    Proveedor= models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    Categoria= models.ForeignKey('Categoria', on_delete=models.CASCADE)
    class Meta:
        db_table="Producto"
        verbose_name="datos del producto"
        verbose_name_plural="Productos"
    def __unicode__ (self):
        return self.id_producto
    def __str__ (self):
        return self.id_producto


class Redes(models.Model):
    id_redes= models.AutoField(primary_key=True)
    instagram= models.CharField(max_length=100, null=True)
    youtube= models.CharField(max_length=100, null=True)
    tik_tok= models.CharField(max_length=100, null=True)
    twitter= models.CharField(max_length=100, null=True)
    twitch= models.CharField(max_length=100, null=True)
    discord= models.CharField(max_length=100, null=True)
    Usuarios= models.CharField(max_length=15, null=True)
    class Meta:
        db_table="Redes"
        verbose_name="Redes socialesr"
        verbose_name_plural="Redes"
    def __unicode__ (self):
        return self.id_redes
    def __str__ (self):
        return self.id_redes

class Registro(models.Model):
    nombre = models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    nombre_usuario=models.CharField(max_length=8)
    email= models.CharField(max_length=25)
    contraseña= models.CharField(max_length=10)
    class Meta:
        db_table="Registro"
        verbose_name="datos de registrados"
        verbose_name_plural="Registros"
    def __unicode__ (self):
        return self.id_registro
    def __str__ (self):
        return self.id_registro
    
class Login(models.Model):
    usuario = models.CharField(max_length=20)
    contraseña= models.CharField(max_length=10)
    class Meta:
        db_table="Login"
        verbose_name="datos de inicio de Sesion"
        verbose_name_plural="Logins"
    def __unicode__ (self):
        return self.id_login
    def __str__ (self):
        return self.id_login

#post_save.connect(create_user_usuarios , sender=User)
#post_save.connect(save_user_usuarios , sender=User)