from django.test import TestCase, RequestFactory
from django.urls import reverse
from usuarios.forms import SignUpForm


from usuarios.models import MyUser

# Create your tests here.

#Comprobando la vista del signUp
class SignUpViewTests (TestCase):
 
    def setUp(self):
        self.factory = RequestFactory()
        self.user = MyUser.objects.create_user(
            email = " test@g.com " ,
            date_of_birth = "1995-01-02",
            password = " 123123b " ,
            first_name = " Test " ,
            last_name = " Apellido "
        )

    def test_db_user(self):
        # Se comprueba que haya sido creado en la tabla Usuario
        self.assertEqual(MyUser.objects.filter(email = "test@g.com").count(), 1)

class SignUpTest(TestCase):
    def test_signup_templates_used(self):
        # testeamos que usamos el template 'usuarios/signup.html'
        response = self.client.get(reverse('SignUp')) #Que puede ir aca!?????
        self.assertTemplateUsed(response, 'usuarios/signup.html')

    def test_signup_view(self):
        # datos en context de la vista
        # por get, llega el form.
        response = self.client.get(reverse('SignUp'))
        self.assertTrue("form" in response.context)
        self.assertTrue(isinstance(response.context["form"], SignUpForm))

    def test_signup_post(self):
        # Que llegan los datos bien por POST
        # que se crea un user nuevo en la db
        #Intento crear un usuario sin setear un campo obligatorio, para probarlo hay q comentar email
        response = self.client.post(reverse('SignUp'), {
            'email' : " test@g.com " ,
            'date_of_birth' : "1995-01-02",
            'password' : " 123123b " ,
            'first_name' : " Test " ,
            'last_name' : " Apellido "
        })

        #Se comprueba que haya sido creado en la tabla User
        self.assertEqual(MyUser.objects.filter(email="test@g.com").count(), 1)
