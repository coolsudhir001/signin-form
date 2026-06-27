// Google Apps Script - Deploy as Web App
// This script handles the form submissions and writes data to Google Sheets

function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    
    // Get the active spreadsheet
    const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    const sheet = spreadsheet.getSheetByName('SignIns') || spreadsheet.getSheets()[0];
    
    // Check if header row exists, if not create it
    if (sheet.getLastRow() === 0) {
      const headers = [
        'Timestamp',
        'Date',
        'Sign-In Time',
        'First Name',
        'Last Name',
        'Email',
        'Student ID',
        'Course',
        'Remarks'
      ];
      sheet.appendRow(headers);
      
      // Format header row
      const headerRange = sheet.getRange(1, 1, 1, headers.length);
      headerRange.setFontWeight('bold');
      headerRange.setBackground('#667eea');
      headerRange.setFontColor('white');
    }
    
    // Prepare the row data
    const rowData = [
      new Date(data.timestamp).toLocaleString(),
      data.date,
      data.signInTime,
      data.firstName,
      data.lastName,
      data.email,
      data.studentId,
      data.course,
      data.remarks || '-'
    ];
    
    // Append data to sheet
    sheet.appendRow(rowData);
    
    // Auto-fit columns
    sheet.autoResizeColumns(1, 9);
    
    return ContentService.createTextOutput(JSON.stringify({
      status: 'success',
      message: 'Data recorded successfully'
    })).setMimeType(ContentService.MimeType.JSON);
    
  } catch (error) {
    Logger.log('Error: ' + error.toString());
    return ContentService.createTextOutput(JSON.stringify({
      status: 'error',
      message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService.createTextOutput('Sign-In Form API is active');
}
