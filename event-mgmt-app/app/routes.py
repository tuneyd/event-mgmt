from flask import render_template, redirect, url_for
from app import app, db
from app.forms import CreateEventForm, EventForm
from app.models import Event

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

# Admin dashboard
@app.route('/admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')

# Create event
@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    form = CreateEventForm()
    if form.validate_on_submit():
        # Create a new event object
        new_event = Event(
            title=form.title.data,
            description=form.description.data
        )
        # Add the event to the database
        db.session.add(new_event)
        db.session.commit()
        # Redirect to the view events page
        return redirect(url_for('view_events'))
    return render_template('create_event.html', form=form)

# View events
@app.route('/view_events')
def view_events():
    events = Event.query.filter_by(is_deleted=False).all()
    return render_template('view_events.html', events=events)


@app.route('/delete_event/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    event.is_deleted = True
    db.session.commit()
    return redirect(url_for('view_events'))

@app.route('/restore_event/<int:event_id>', methods=['POST'])
def restore_event(event_id):
    event = Event.query.get_or_404(event_id)
    event.is_deleted = False
    db.session.commit()
    # Optionally, you can add a flash message here to inform the user that the event has been restored.
    return redirect(url_for('view_events'))

@app.route('/edit_event/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)
    form = EventForm(obj=event)
    if form.validate_on_submit():
        event.title = form.title.data
        event.description = form.description.data
        db.session.commit()
        return redirect(url_for('view_events'))
    return render_template('edit_event.html', form=form)
