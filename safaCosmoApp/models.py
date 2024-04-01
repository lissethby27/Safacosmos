from django.db import models

# Create your models here.
class Carrito(models.Model):
    id = models.AutoField(primary_key=True)

class Talla(models.Model):
    nombre = models.CharField(max_length=2)

class Complemento(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    color = models.CharField(max_length=100)
    talla = models.ForeignKey(Talla, on_delete=models.DO_NOTHING, null=True)
    nombre = models.CharField(max_length=150)
    tipo = models.CharField(max_length=100)
    stock = models.IntegerField()


class ComplementoCarrito(models.Model):
    carrito = models.OneToOneField(Carrito, on_delete=models.CASCADE, primary_key=True)
    complemento = models.ForeignKey(Complemento, on_delete=models.CASCADE)


class Fenomeno(models.Model):
    nombre = models.CharField(max_length=150)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=500)


class SalaChat(models.Model):
    fechaConversacion = models.DateTimeField()


class Estadistica(models.Model):
    mediaValoracion = models.FloatField()


class Encuentro(models.Model):
    lugar = models.CharField(max_length=200)
    horaInicio = models.DateTimeField()
    horaFinal = models.DateTimeField()
    salaChat = models.ForeignKey(SalaChat, on_delete=models.CASCADE)
    fenomeno = models.ForeignKey(Fenomeno, on_delete=models.CASCADE)


class Usuario(models.Model):
    nick = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    sala_chat = models.ForeignKey(SalaChat, on_delete=models.CASCADE)
    encuentro = models.ForeignKey(Encuentro, on_delete=models.CASCADE)

class UsuarioComplemento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    complemento = models.ForeignKey(Complemento, on_delete=models.CASCADE)



class Valoracion(models.Model):
    puntuacion = models.IntegerField()
    comentario = models.CharField(max_length=250)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estadistica = models.ForeignKey(Estadistica, on_delete=models.CASCADE)


class Mensaje(models.Model):
    fecha = models.DateTimeField()
    info = models.CharField(max_length=250)
    sala_chat = models.ForeignKey(SalaChat, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)



