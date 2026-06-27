# Student Sign-In Form

A modern, responsive web form that collects student sign-in data and automatically sends it to a Google Spreadsheet.

## ✨ Features

- ✅ Responsive design (desktop & mobile)
- ✅ Collects student information (name, email, ID, course, time, date, remarks)
- ✅ Automatic timestamp recording
- ✅ Real-time form validation
- ✅ Sends data directly to Google Sheets
- ✅ Success/error messaging with loading states
- ✅ Auto-formatted spreadsheet with headers
- ✅ Beautiful gradient UI with smooth animations

## 📁 Files Included

- `index.html` - Form structure and layout
- `styles.css` - Responsive styling and animations
- `script.js` - Form handling and validation
- `google-apps-script.gs` - Backend for Google Sheets integration
- `README.md` - Documentation

## 🚀 Quick Setup Guide

### Step 1: Create a Google Spreadsheet

1. Go to [Google Sheets](https://sheets.google.com)
2. Create a new spreadsheet
3. Name it "Student Sign-In" (optional)
4. Rename the first sheet tab to "SignIns" (optional - script will auto-create headers)

### Step 2: Set Up Google Apps Script

1. In your Google Spreadsheet, click **Tools → Script Editor**
2. Delete the default code
3. Copy and paste the entire contents of `google-apps-script.gs`
4. Save the project (Ctrl+S or Cmd+S)
5. Name it "Student Sign-In" when prompted

### Step 3: Deploy as Web App

1. Click the **Deploy** button (top right)
2. Select **New deployment**
3. Click the gear icon, then select **Web app**
4. Configure:
   - **Execute as:** Your Google Account
   - **Who has access:** Anyone
5. Click **Deploy**
6. A dialog will appear. Click **Authorize access**
7. Review permissions and select your Google account
8. Click **Allow**
9. Copy the deployment URL that appears

**Example URL:** `https://script.google.com/macros/d/YOUR_ID_HERE/userweb?v=1`

### Step 4: Update the Form

1. Open `script.js` in your repository
2. Find this line: `const GOOGLE_SCRIPT_URL = 'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE';`
3. Replace `'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE'` with your actual deployment URL
4. Save the file

### Step 5: Host the Form Online

#### Option A: GitHub Pages (Free & Easy)
1. Your files are already in GitHub
2. Go to repository **Settings → Pages**
3. Under "Source", select **main** branch
4. Click **Save**
5. Your form will be live at `https://coolsudhir001.github.io/signin-form/`

#### Option B: Netlify (Free)
1. Go to [Netlify](https://netlify.com)
2. Drag and drop your project folder, or connect your GitHub repo
3. Your form will be deployed automatically

#### Option C: Other Web Servers
- Upload `index.html`, `styles.css`, and `script.js` to any web hosting

## 📋 Form Fields

The form collects:

| Field | Type | Required |
|-------|------|----------|
| First Name | Text | Yes |
| Last Name | Text | Yes |
| Email Address | Email | Yes |
| Student ID | Text | Yes |
| Course/Class | Text | Yes |
| Sign-In Time | Time | Yes |
| Date | Date | Yes |
| Remarks | Textarea | No |

Plus automatic:
- Submission timestamp (UTC)

## 🔧 How It Works

1. Student fills out the form
2. Clicks "Sign In" button
3. JavaScript collects all form data
4. Data is sent to Google Apps Script via POST request
5. Script receives the data and adds it to the spreadsheet
6. New row is automatically formatted with headers
7. Student sees success confirmation
8. Form resets with current date/time

## 📊 Spreadsheet Output

Your Google Sheet will look like:

| Timestamp | Date | Sign-In Time | First Name | Last Name | Email | Student ID | Course | Remarks |
|-----------|------|--------------|-----------|----------|-------|-----------|--------|---------|
| 6/27/2026, 2:45:30 PM | 2026-06-27 | 14:45 | John | Doe | john@email.com | STU001 | CS101 | Present |

## 🎨 Customization

### Add More Form Fields

1. Add field to `index.html`:
```html
<div class="form-group">
    <label for="fieldName">Label</label>
    <input type="text" id="fieldName" name="fieldName" required>
</div>
```

2. Update `script.js` to include it in formData:
```javascript
fieldName: document.getElementById('fieldName').value.trim(),
```

3. Update `google-apps-script.gs` headers and rowData arrays:
```javascript
headers = [..., 'Field Name'];
rowData = [..., data.fieldName];
```

### Change Colors

Edit `styles.css` gradient colors:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Change to your preferred colors. Examples:
- Teal: `#0084ff` to `#00d4ff`
- Orange: `#ff6b6b` to `#ff8c42`
- Green: `#4caf50` to `#45b393`

## 🐛 Troubleshooting

### Form not submitting?
- ✅ Check browser console (F12) for error messages
- ✅ Verify `GOOGLE_SCRIPT_URL` is set correctly in `script.js`
- ✅ Ensure Google Apps Script is deployed as "Web app"
- ✅ Check that "Who has access" is set to "Anyone"

### Data not appearing in spreadsheet?
- ✅ Verify deployment URL is correct
- ✅ Check Google Apps Script has proper authorization
- ✅ Ensure sheet name is "SignIns" (or update in script)
- ✅ Check the script's Execution log (Tools → Execution log)

### CORS errors in console?
- This is normal with `mode: 'no-cors'`
- The data will still submit successfully
- The browser restricts reading the response, but the server receives it

### Changes not showing up?
- Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
- Clear browser cache
- Check you're editing the right file

## 🔐 Security Considerations

- The Google Apps Script is set to "Anyone" for easy setup
- For production/institutional use, consider:
  - Adding authentication/login
  - Restricting to specific email domains
  - Adding rate limiting
  - Validating data server-side
  - Using restricted deployment URLs

## 📱 Browser Support

- ✅ Chrome/Edge (all versions)
- ✅ Firefox (all versions)
- ✅ Safari (10+)
- ⚠️ Internet Explorer (not recommended)

## 💡 Tips & Tricks

- **Auto-fill date/time**: Form auto-fills today's date and current time
- **Clear fields**: After successful submission, form automatically clears
- **Prevent duplicate submissions**: Submit button disables during submission
- **Mobile-friendly**: Form is fully responsive on phones and tablets
- **Keyboard navigation**: Use Tab to navigate fields, Enter to submit

## 📞 Support

For issues:
1. Check the Troubleshooting section above
2. Review Google Apps Script Execution log
3. Check browser console for error messages (F12)
4. Verify all URLs and IDs are correct

## 📄 License

Free to use and modify for educational purposes.

---

**Happy Sign-Ins! 🎓**
