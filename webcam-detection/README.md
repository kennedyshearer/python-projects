# Webcam Motion Detection with Email Alerts

A Python application that uses your computer's webcam to detect motion and automatically sends email alerts with captured images when movement is detected.

## 🎯 Features

- **Real-time Motion Detection**: Uses OpenCV to capture video from your webcam and detect movement
- **Smart Object Detection**: Filters out small movements (less than 5000 pixels) to reduce false alarms
- **Automatic Email Alerts**: Sends email notifications with attached images when motion is detected
- **Image Management**: Automatically saves and cleans up captured images
- **Multi-threaded**: Uses threading for non-blocking email sending and folder cleanup

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.6 or higher
- A working webcam
- Gmail account with App Password (for sending emails)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/app9-email-webcam-detection.git
   cd app9-email-webcam-detection
   ```

2. **Install required dependencies**:
   ```bash
   pip install opencv-python
   pip install filetype
   ```

## ⚙️ Configuration

### Email Setup

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate an App Password**:
   - Go to Google Account settings
   - Navigate to Security → 2-Step Verification → App passwords
   - Generate a new app password for "Mail"
3. **Update the email configuration** in `emailing.py`:
   ```python
   PASSWORD = "your_app_password_here"
   SENDER = "your_email@gmail.com"
   RECEIVER = "recipient_email@gmail.com"
   ```

## 🚀 Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **The application will**:
   - Open your webcam feed
   - Show a window with motion detection overlay
   - Display a threshold window showing detected motion
   - Automatically send emails when motion is detected

3. **To exit the application**:
   - Press `q` in any of the video windows

## 📁 Project Structure

```
app9-email-webcam-detection/
├── main.py              # Main application with motion detection logic
├── emailing.py          # Email functionality
├── images/              # Directory for captured images (auto-created)
└── README.md           # This file
```

## 🔧 How It Works

1. **Motion Detection**: The application captures frames from your webcam and compares them to detect movement using frame differencing
2. **Object Filtering**: Only objects larger than 5000 pixels trigger alerts (reduces false positives)
3. **Image Capture**: When motion is detected, the current frame is saved as a PNG image
4. **Email Alert**: An email with the captured image is sent to the configured recipient
5. **Cleanup**: The images folder is automatically cleaned after sending the email

## ⚠️ Important Notes

- **Privacy**: This application captures images from your webcam. Ensure you're aware of what's being recorded
- **Email Security**: Use App Passwords, not your regular Gmail password
- **Performance**: The application runs continuously and may use significant CPU resources
- **Storage**: Images are temporarily stored and automatically cleaned up

## 🛡️ Security Considerations

- Never commit your email password to version control
- Consider using environment variables for sensitive data
- Be mindful of what your webcam captures
- Ensure your email account has proper security settings

## ⚡ Troubleshooting

### Common Issues

1. **Webcam not working**: Ensure your webcam is not being used by another application
2. **Email not sending**: Check your Gmail App Password and 2FA settings
3. **High CPU usage**: This is normal for real-time video processing
4. **False alarms**: Adjust the contour area threshold in `main.py` (currently 5000)

### Dependencies Issues

If you encounter issues with OpenCV:
```bash
pip uninstall opencv-python
pip install opencv-python-headless
```