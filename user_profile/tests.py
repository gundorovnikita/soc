{% extends 'base.html' %}
{% load static %}
<head>
  <link href="{% static 'css/blog.css' %}" rel="stylesheet">
</head>
{% block content %}
  <form method='post'>
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit">
  </form>
{% endblock %}
