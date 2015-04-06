Name:           ros-hydro-python-trep
Version:        1.0.0
Release:        0%{?dist}
Summary:        ROS python_trep package

Group:          Development/Libraries
License:        GPLv3
URL:            http://nxr.northwestern.edu/trep
Source0:        %{name}-%{version}.tar.gz

Requires:       PyOpenGL
Requires:       PyQt4
Requires:       PyQt4-devel
Requires:       freeglut-devel
Requires:       numpy
Requires:       python-devel
Requires:       python-matplotlib
Requires:       python-pillow
Requires:       python-pillow-qt
Requires:       ros-hydro-rospy
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-tf
Requires:       scipy
Requires:       sip-devel
BuildRequires:  PyOpenGL
BuildRequires:  PyQt4
BuildRequires:  PyQt4-devel
BuildRequires:  freeglut-devel
BuildRequires:  numpy
BuildRequires:  python-devel
BuildRequires:  python-matplotlib
BuildRequires:  python-pillow
BuildRequires:  python-pillow-qt
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-rospy
BuildRequires:  scipy
BuildRequires:  sip-devel

%description
Trep: Mechanical Simulation and Optimal Control Software

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Apr 06 2015 Jarvis Schultz <jschultz@northwestern.edu> - 1.0.0-0
- Autogenerated by Bloom

* Mon Dec 01 2014 Jarvis Schultz <jschultz@northwestern.edu> - 0.93.1-0
- Autogenerated by Bloom

