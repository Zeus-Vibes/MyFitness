# Quick Start Guide - FitLife Fitness Website

## Getting Started in 5 Minutes

### Step 1: Start the Server
```bash
cd fitness_website
python manage.py runserver
```

### Step 2: Access the Website
Open your browser and go to: **http://127.0.0.1:8000**

### Step 3: Login as Admin
1. Click "Login" in the top navigation
2. Use credentials:
   - **Username:** `admin`
   - **Password:** `admin`

### Step 4: Access Admin Panel
1. After logging in, click your username in the top right
2. Select "Admin Panel" from the dropdown
3. You're now in the admin dashboard!

## What You Can Do

### As a Regular User
✅ Browse workout plans and exercises  
✅ View diet plans with nutritional info  
✅ Calculate your BMI  
✅ Calculate daily calorie needs  
✅ Track your fitness journey  

### As an Administrator
✅ Manage all users  
✅ Create workout plans  
✅ Add exercises with videos  
✅ Design diet plans  
✅ View platform statistics  
✅ Search and filter content  

## Quick Navigation

### Public Pages
- **Home:** http://127.0.0.1:8000/
- **Workouts:** http://127.0.0.1:8000/workouts/
- **Exercises:** http://127.0.0.1:8000/workouts/exercises/
- **Diet Plans:** http://127.0.0.1:8000/nutrition/
- **BMI Calculator:** http://127.0.0.1:8000/calculators/bmi/
- **Calorie Calculator:** http://127.0.0.1:8000/calculators/calories/

### Admin Pages (Login Required)
- **Admin Dashboard:** http://127.0.0.1:8000/admin-panel/
- **User Management:** http://127.0.0.1:8000/admin-panel/users/
- **Workout Management:** http://127.0.0.1:8000/admin-panel/workouts/
- **Exercise Management:** http://127.0.0.1:8000/admin-panel/exercises/
- **Diet Plan Management:** http://127.0.0.1:8000/admin-panel/diet-plans/

## Sample Data Included

The database comes pre-populated with:
- ✅ 5 Sample Exercises (Push-ups, Squats, Deadlifts, Plank, Burpees)
- ✅ 1 Beginner Workout Plan with 3 sessions
- ✅ 6 Food Items (Chicken, Rice, Broccoli, Salmon, Sweet Potato, Yogurt)
- ✅ 1 Balanced Diet Plan with sample meals
- ✅ 1 Admin User (username: admin, password: admin)

## Common Tasks

### Create a New User
1. Go to Admin Panel → User Management
2. Click "Add New User"
3. Fill in username, email, password
4. Assign role (User, Trainer, or Admin)
5. Click "Create User"

### Add an Exercise
1. Go to Admin Panel → Exercises
2. Click "Add Exercise"
3. Enter exercise name and description
4. Add muscle groups and equipment
5. Paste YouTube video URL
6. Write instructions
7. Click "Create Exercise"

### Create a Workout Plan
1. Go to Admin Panel → Workout Plans
2. Click "Create Workout Plan"
3. Enter plan details
4. Select difficulty and goal
5. Set duration in weeks
6. Click "Create Workout Plan"

### Design a Diet Plan
1. Go to Admin Panel → Diet Plans
2. Click "Create Diet Plan"
3. Enter plan name and description
4. Set daily calorie target
5. Adjust macro percentages (must equal 100%)
6. Click "Create Diet Plan"

## Tips for Success

### For Users
- 📝 Complete your profile with fitness goals
- 📊 Use calculators to track your metrics
- 🎯 Follow workout and diet plans consistently
- 📹 Watch exercise videos for proper form

### For Admins
- 🔍 Use search and filters to find content quickly
- ✅ Verify data before saving (especially macro percentages)
- 📺 Always include YouTube videos for exercises
- 📈 Monitor dashboard statistics regularly
- 👥 Keep user information up-to-date

## Troubleshooting

### Can't Login?
- Check username and password (case-sensitive)
- Default admin: username `admin`, password `admin`
- Clear browser cache and try again

### Can't Access Admin Panel?
- Make sure you're logged in
- Your account must have Admin or Superuser role
- Check the dropdown menu under your username

### Forms Not Saving?
- Check for validation errors (red text)
- Ensure all required fields are filled
- For diet plans, macros must equal 100%
- Passwords must match when creating users

### Page Not Loading?
- Verify the server is running
- Check the URL is correct
- Try refreshing the page
- Check browser console for errors

## Next Steps

### Explore the Platform
1. Browse the sample workout plans
2. Check out the exercise library
3. View the diet plans
4. Try the calculators

### Customize Content
1. Add your own exercises
2. Create custom workout plans
3. Design personalized diet plans
4. Add more food items

### Manage Users
1. Create test user accounts
2. Assign different roles
3. Update user profiles
4. Monitor user activity

## Need Help?

📖 **Full Documentation:**
- See `README.md` for complete features
- See `ADMIN_PANEL_GUIDE.md` for detailed admin instructions

🔧 **Technical Issues:**
- Check Django error logs
- Verify migrations are up-to-date: `python manage.py migrate`
- Ensure all dependencies are installed: `pip install -r requirements.txt`

💡 **Feature Requests:**
- The platform is designed to be extensible
- Check the "Future Enhancements" section in the guides
- Customize as needed for your specific requirements

## Security Notes

⚠️ **Important for Production:**
- Change the default admin password immediately
- Update `SECRET_KEY` in settings.py
- Set `DEBUG = False` in production
- Use environment variables for sensitive data
- Enable HTTPS
- Configure proper database (PostgreSQL recommended)
- Set up regular backups

## Quick Reference

### Default Credentials
- **Username:** admin
- **Password:** admin
- **Role:** Superuser/Admin

### Port
- **Development Server:** http://127.0.0.1:8000

### Database
- **Type:** SQLite (default)
- **Location:** `db.sqlite3`

### Static Files
- **CSS/JS:** Bootstrap 5, Font Awesome, Chart.js
- **CDN-based:** No local static files needed

---

**Ready to get started? Fire up the server and explore!** 🚀