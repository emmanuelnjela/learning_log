from django.shortcuts import render, redirect
from .models import Entry, Topic
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """Home page for Learning Logs"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """A page for all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """A page for a single topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Add a new topic form"""
    if request.method != 'POST':
        # no data submitted; return the blank form
        form = TopicForm()
    else:
        # POST data submitted; process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
        
    # Display blank or valid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Adding new Entry"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        # no data submitted; create blank form
        form = EntryForm()
    else:
        # POST data submitted; process data
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    
    # display blank or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """Editing an entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # intial request; prefill the form with the existing entry data
        form = EntryForm(instance=entry)
    
    else:
        # POST data submitted; process data
        form = EntryForm(instance=Entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    
    context = {'entry': entry, 'form': form, 'topic': topic}
    return render(request, 'learning_logs/new_entry.html', context)
