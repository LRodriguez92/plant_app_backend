# Plant App Backend API

|      Verb      | Endpoint                 | Description                                   |
| :-------------:| :----------              | :-----------                                  |
|  GET           | /plants/                 | View all of the plants the user owns          |
|  GET           | /plants/:pk/             | View a specific plant                         |
|  GET           | /plants/:pk/images/      | View all images for specific plant            |
|  GET           | /plants/:pk/images/:pk/  | View a specific image for a specific plant    |
|  GET           | /plants/:pk/schedule/    | View the schedule for a specific plant        |
|  POST          | /users/                  | Create User                                   |
|  POST          | /token/                  | Login User                                    |
|  POST          | /plants/                 | Create a Plant for the user                   |
|  POST          | /plants/:pk/images/      | Add an image for a specific plant             |
|  POST          | /plants/:pk/schedule/    | Add a schedule for a specific plant           |
|  POST          | /trefle/plants/:name     | Search plant info in trefle api               |
|  PUT           | /plants/:pk/             | Edit a specific plant's information           |
|  PUT           | /plants/:pk/images/:pk/  | Edit a specific image for a specific plant    |
|  PUT           | /plants/:pk/schedule/    | Edit the schedule for a specific plant        |
|  PUT           | /users/:pk/profile/      | Edit User Profile info                        |
|  DELETE        | /plants/:pk/             | Delete a specific plant                       |
|  DELETE        | /plants/:pk/images/:pk/  | Delete a specific image for a specific plant  |
|  DELETE        | /plants/:pk/schedule/    | Delete the schedule for a specific plant      |
