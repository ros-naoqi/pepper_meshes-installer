Name:           ros-kinetic-pepper-meshes
Version:        0.2.3
Release:        2%{?dist}
Summary:        ROS pepper_meshes package

Group:          Development/Libraries
License:        Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License
URL:            http://github.com/ros-naoqi/pepper_meshes/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  java-1.8.0-openjdk
BuildRequires:  ros-kinetic-catkin

%description
meshes for the Aldebaran Robotics Pepper

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Sep 19 2016 Mikael Arguedas <mikael.arguedas@gmail.com> - 0.2.3-2
- Autogenerated by Bloom

* Mon Sep 19 2016 Mikael Arguedas <mikael.arguedas@gmail.com> - 0.2.3-1
- Autogenerated by Bloom

* Thu Jun 16 2016 Mikael Arguedas <mikael.arguedas@gmail.com> - 0.2.3-0
- Autogenerated by Bloom

