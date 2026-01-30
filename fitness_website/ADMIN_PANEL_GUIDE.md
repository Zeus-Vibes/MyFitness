# Admin Panel Guide - FitLife Fitness Website

## Overview
The FitLife Admin Panel is a comprehensive management system for administrators to manage users, workout plans, exercises, diet plans, and monitor platform statistics.

## Access Requirements

### Admin Access
- **URL:** `http://127.0.0.1:8000/admin-panel/`
- **Required Role:** Admin or Superuser
- **Default Admin:** username: `admin`, password: `admin`

### User Roles
1. **User** - Regular members with basic access
2. **Trainer** - Can manage workout plans and exercises (future feature)
3. **Admin** - Full system access including user management

## Features

### 1. Dashboard (`/admin-panel/`)
**Statistics Overview:**
- Total users and active members
- Workout plans and exercises count
- Diet plans and food items
- BMI and calorie calculations

**Visual Analytics:**
- User role distribution chart
- Recent activity feeds
- Quick action buttons

**Recent Activity:**
- Latest registered users
- Recently created workout plans
- New diet plans

### 2. User Management (`/admin-panel/users/`)

**User List Features:**
- Search by username, name, or email
- Filter by user role
- Pagination (20 users per page)
- View user details, edit, or delete

**User Creation/Editing:**
- Basic information (username, email, name)
- Password management
- Role assignment
- Contact information (phone, date of birth)
- Fitness information (age, height, weight, goals)
- Membership status and dates

**User Detail View:**
- Complete user profile
- Activity summary (workouts, diet plans, calculations)
- Membership information
- Quick edit access

### 3. Workout Plan Management (`/admin-panel/workouts/`)

**Workout List Features:**
- Search by name or description
- Filter by difficulty level (Beginner, Intermediate, Advanced)
- Filter by goal (Weight Loss, Muscle Gain, Strength, Endurance)
- Card-based responsive layout
- Pagination (12 plans per page)

**Workout Creation/Editing:**
- Plan name and description
- Difficulty level selection
- Duration in weeks
- Goal assignment
- Form validation

**Workout Detail View:**
- Complete plan information
- All workout sessions listed
- Exercise breakdown per session
- Usage statistics (users following the plan)
- Quick actions (edit, duplicate, delete)

### 4. Exercise Management (`/admin-panel/exercises/`)

**Exercise List Features:**
- Search by name, description, or muscle groups
- Filter by muscle group
- Table view with key information
- Direct links to YouTube videos
- Pagination (15 exercises per page)

**Exercise Creation/Editing:**
- Exercise name and description
- Muscle groups targeted
- Equipment needed
- YouTube video URL
- Step-by-step instructions
- Video preview (on edit page)

**Exercise Guidelines:**
- Common muscle group combinations
- Equipment types
- Instruction formatting tips

### 5. Diet Plan Management (`/admin-panel/diet-plans/`)

**Diet Plan List Features:**
- Search by name or description
- Filter by goal (Weight Loss, Muscle Gain, Maintenance)
- Card-based layout with macro visualization
- Pagination (12 plans per page)

**Diet Plan Creation/Editing:**
- Plan name and description
- Goal selection
- Daily calorie target
- Macronutrient distribution (Protein, Carbs, Fat)
- Real-time macro percentage calculator
- Validation (must equal 100%)

**Diet Plan Guidelines:**
- Common macro splits for different goals
- Calorie recommendations
- Nutritional best practices

## Navigation

### Sidebar Menu
- **Dashboard** - Main overview
- **User Management** - Manage all users
- **Workout Plans** - Manage workout programs
- **Exercises** - Exercise library management
- **Diet Plans** - Nutrition plan management
- **Back to Website** - Return to public site
- **Logout** - Sign out

### Quick Actions
Available on dashboard for rapid access:
- Add New User
- Create Workout Plan
- Add Exercise
- Create Diet Plan

## Common Tasks

### Creating a New User
1. Navigate to User Management
2. Click "Add New User"
3. Fill in required fields (username, email, password)
4. Assign role (User, Trainer, or Admin)
5. Add optional fitness information
6. Click "Create User"

### Creating a Workout Plan
1. Navigate to Workout Plans
2. Click "Create Workout Plan"
3. Enter plan details (name, description, difficulty, duration, goal)
4. Click "Create Workout Plan"
5. Add workout sessions and exercises (from detail view)

### Creating an Exercise
1. Navigate to Exercises
2. Click "Add Exercise"
3. Enter exercise details
4. Add YouTube video URL for demonstration
5. Write step-by-step instructions
6. Click "Create Exercise"

### Creating a Diet Plan
1. Navigate to Diet Plans
2. Click "Create Diet Plan"
3. Enter plan details and daily calories
4. Set macronutrient percentages (must total 100%)
5. Watch the real-time calculator
6. Click "Create Diet Plan"

## Search and Filtering

### User Search
- Search by: username, first name, last name, email
- Filter by: role (User, Trainer, Admin)

### Workout Search
- Search by: plan name, description
- Filter by: difficulty level, goal

### Exercise Search
- Search by: exercise name, description, muscle groups
- Filter by: muscle group

### Diet Plan Search
- Search by: plan name, description
- Filter by: goal

## Bulk Operations

### Delete Operations
- Individual delete buttons on list views
- Confirmation dialog before deletion
- AJAX-based deletion (no page reload)
- Cannot delete your own admin account

## Data Validation

### User Forms
- Username uniqueness
- Email format validation
- Password strength requirements
- Password confirmation matching

### Workout Forms
- Required fields validation
- Duration must be positive
- Difficulty and goal selection required

### Exercise Forms
- Name uniqueness recommended
- YouTube URL format validation
- Instructions required

### Diet Plan Forms
- Macro percentages must equal 100%
- Daily calories must be positive
- Real-time validation feedback

## Security Features

### Authentication
- Login required for all admin pages
- Role-based access control
- Admin/Superuser verification

### Authorization
- User role checking on every request
- Redirect to login if not authenticated
- Redirect to home if not admin

### CSRF Protection
- All forms include CSRF tokens
- AJAX requests include CSRF headers
- Django's built-in CSRF middleware

## UI/UX Features

### Responsive Design
- Mobile-friendly interface
- Bootstrap 5 framework
- Responsive tables and cards
- Collapsible sidebar on mobile

### Visual Feedback
- Success/error messages
- Loading indicators
- Confirmation dialogs
- Color-coded badges and alerts

### Accessibility
- Semantic HTML
- ARIA labels
- Keyboard navigation
- Screen reader friendly

## Tips and Best Practices

### User Management
- Assign appropriate roles based on responsibilities
- Keep user information up-to-date
- Monitor active membership status
- Review user activity regularly

### Content Management
- Use clear, descriptive names
- Write detailed descriptions
- Include YouTube videos for exercises
- Test workout plans before publishing

### Data Integrity
- Regularly backup database
- Verify macro percentages before saving
- Check exercise instructions for accuracy
- Review user feedback on plans

### Performance
- Use search and filters to find content quickly
- Pagination keeps pages loading fast
- AJAX operations reduce page reloads
- Optimize images and videos

## Troubleshooting

### Cannot Access Admin Panel
- Verify you're logged in
- Check your user role (must be Admin or Superuser)
- Clear browser cache and cookies
- Try logging out and back in

### Form Validation Errors
- Check all required fields are filled
- Verify percentages add to 100% (diet plans)
- Ensure passwords match
- Check for duplicate usernames/emails

### Delete Operations Failing
- Cannot delete your own account
- Check for dependencies (users with active plans)
- Verify CSRF token is present
- Check browser console for errors

## Future Enhancements

### Planned Features
- Workout session builder
- Meal planning interface
- Bulk import/export
- Advanced analytics and reports
- User activity logs
- Email notifications
- Content approval workflow
- Multi-language support

## Support

For issues or questions:
1. Check this guide first
2. Review Django error logs
3. Check browser console for JavaScript errors
4. Verify database migrations are up-to-date

## Technical Details

### Technology Stack
- Django 4.2+
- Bootstrap 5.1.3
- Font Awesome 6.0
- Chart.js for analytics
- jQuery for AJAX operations

### File Structure
```
admin_panel/
├── views.py          # All view functions
├── forms.py          # Form definitions
├── urls.py           # URL routing
└── templates/
    └── admin_panel/
        ├── base_admin.html       # Base template
        ├── dashboard.html        # Main dashboard
        ├── user_list.html        # User management
        ├── user_form.html        # User create/edit
        ├── user_detail.html      # User details
        ├── workout_list.html     # Workout management
        ├── workout_form.html     # Workout create/edit
        ├── workout_detail.html   # Workout details
        ├── exercise_list.html    # Exercise management
        ├── exercise_form.html    # Exercise create/edit
        ├── diet_plan_list.html   # Diet management
        └── diet_plan_form.html   # Diet create/edit
```

### Database Models
- CustomUser (extended Django User)
- WorkoutPlan, WorkoutSession, WorkoutExercise
- Exercise
- DietPlan, Meal, MealFood, Food
- BMICalculation, CalorieCalculation

## Changelog

### Version 1.0 (Current)
- Initial admin panel release
- User management with CRUD operations
- Workout plan management
- Exercise library management
- Diet plan management
- Dashboard with statistics
- Search and filtering
- Responsive design
- Role-based access control