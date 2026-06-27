// Replace with your Google Apps Script Web App URL
const GOOGLE_SCRIPT_URL = 'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE';

const form = document.getElementById('signinForm');
const messageDiv = document.getElementById('message');

// Set today's date as default
document.getElementById('date').valueAsDate = new Date();

// Set current time as default
const now = new Date();
document.getElementById('signInTime').value = now.getHours().toString().padStart(2, '0') + ':' + 
                                                now.getMinutes().toString().padStart(2, '0');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Validate that Google Script URL is set
    if (GOOGLE_SCRIPT_URL === 'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE') {
        showMessage('Please configure the Google Apps Script URL first', 'error');
        return;
    }

    // Show loading message
    showMessage('Submitting...', 'loading');
    
    // Disable submit button
    const submitBtn = form.querySelector('.btn-submit');
    submitBtn.disabled = true;

    try {
        // Collect form data
        const formData = {
            firstName: document.getElementById('firstName').value.trim(),
            lastName: document.getElementById('lastName').value.trim(),
            email: document.getElementById('email').value.trim(),
            studentId: document.getElementById('studentId').value.trim(),
            course: document.getElementById('course').value.trim(),
            signInTime: document.getElementById('signInTime').value,
            date: document.getElementById('date').value,
            remarks: document.getElementById('remarks').value.trim(),
            timestamp: new Date().toISOString()
        };

        // Send data to Google Apps Script
        const response = await fetch(GOOGLE_SCRIPT_URL, {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        // Show success message
        showMessage('✓ Sign-in successful! Your data has been recorded.', 'success');
        
        // Reset form
        form.reset();
        
        // Reset date and time to current values
        document.getElementById('date').valueAsDate = new Date();
        const now = new Date();
        document.getElementById('signInTime').value = now.getHours().toString().padStart(2, '0') + ':' + 
                                                      now.getMinutes().toString().padStart(2, '0');

        // Hide message after 3 seconds
        setTimeout(() => {
            messageDiv.classList.remove('show');
        }, 3000);

    } catch (error) {
        console.error('Error:', error);
        showMessage('✗ Error submitting form. Please try again.', 'error');
    } finally {
        // Re-enable submit button
        submitBtn.disabled = false;
    }
});

function showMessage(text, type) {
    messageDiv.textContent = text;
    messageDiv.className = `message show ${type}`;
}
