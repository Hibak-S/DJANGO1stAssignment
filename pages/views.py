from django.shortcuts import render


# View for the Homepage
def index_view(request):
    # The context dictionary to pass data to the template
    context = {
        "student_name": "HIBAQ sAHAL",
        "tagline": "Aspiring Django Developer building my first MVT site!",
    }
    # Render the request, using the specified template and context
    return render(request, "index.html", context)


# View for the Education Page
def education_view(request):
    # A separate context for this page
    context = {
        "school_name": "Refactory Academy",
        "graduation_year": 2025,
    }
    # Render this view's template
    return render(request, "education.html", context)
