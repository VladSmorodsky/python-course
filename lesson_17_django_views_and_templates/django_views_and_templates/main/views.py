from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


# Create your views here.

def home(request: HttpRequest) -> HttpResponse:
    """
    Home page
    :param request:
    :return:
    """
    return render(request, "main/home.html", {
        'page_name': 'home',
    })


def about(request: HttpRequest) -> HttpResponse:
    """
    About page, describe our missions
    :param request:
    :return:
    """
    mission_list = [
        'Delivering Excellence – Creating reliable, scalable, and user-friendly software tailored to client needs.',
        'Innovating Continuously – Staying ahead of the curve with the latest technologies and development practices.',
        'Ensuring Customer Success – Providing top-tier support and collaboration to help businesses thrive.',
        'Building a Tech-Driven Future – Driving digital transformation through cutting-edge software solutions.'
    ]
    return render(request, 'main/about.html', {
        'page_name': 'about',
        'mission_list': mission_list,
    })


class ServicesView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Render services page
        :param request:
        :return:
        """
        service_list = [
            {
                'title': 'Custom Software Development',
                'content': 'We design and develop tailored software solutions to meet your unique business requirements, ensuring scalability and performance.'
            },
            {
                'title': 'Web Development',
                'content': 'From dynamic websites to complex web applications, we create responsive, high-performance, and secure web solutions.'
            },
            {
                'title': 'Mobile App Development',
                'content': 'We build intuitive and feature-rich mobile applications for iOS and Android, enhancing user engagement and business reach.'
            },
            {
                'title': 'E-commerce Solutions',
                'content': 'Our team develops robust e-commerce platforms with secure payment integration, inventory management, and seamless user experience.'
            },
            {
                'title': 'Cloud Solutions',
                'content': 'Leverage the power of cloud computing with our scalable cloud-based applications and infrastructure solutions.'
            },
            {
                'title': 'API Development & Integration',
                'content': 'We create and integrate powerful APIs to enhance functionality and connectivity across different systems and platforms.'
            },
            {
                'title': 'UI/UX Design',
                'content': 'Our design team focuses on creating visually appealing and user-friendly interfaces for enhanced digital experiences.'
            },
            {
                'title': 'IT Consulting & Support',
                'content': 'We offer expert guidance on software architecture, technology stack selection, and ongoing system support to optimize performance.'
            }
        ]
        return render(request, 'main/services.html', {
            'page_name': 'services',
            'service_list': service_list,
        })


class ContactsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Render contacts page
        :param request:
        :return:
        """
        return render(request, 'main/contacts.html', {
            'page_name': 'contacts',
        })
