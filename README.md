
## Project Description

Provide a brief overview of your project, including its purpose and functionality.

## API Endpoints

### 1. User Profiles

#### 1.1 Get All User Profiles

- **Endpoint**: `/api/userprofiles/`
- **HTTP Method**: GET
- **Description**: Get a list of all user profiles.
- **Parameters**: None
- **Response**: List of user profiles.

#### 1.2 Get User Profile by ID

- **Endpoint**: `/api/userprofiles/{id}/`
- **HTTP Method**: GET
- **Description**: Get a user profile by ID.
- **Parameters**: `id` (User Profile ID)
- **Response**: User profile details.

#### 1.3 Update User Profile

- **Endpoint**: `/api/userprofiles/{id}/`
- **HTTP Method**: PUT
- **Description**: Update a user profile.
- **Parameters**: `id` (User Profile ID)
- **Request Body**: User profile data.
- **Response**: Updated user profile details.

#### 1.4 Update User Profile Image

- **Endpoint**: `/api/userprofiles/{id}/update_profile_image/`
- **HTTP Method**: PUT
- **Description**: Update the user profile image.
- **Parameters**: `id` (User Profile ID)
- **Request Body**: User profile image data.
- **Response**: Updated user profile details.
