# Script generated with Bloom
pkgdesc="ROS - Trep: Mechanical Simulation and Optimal Control Software"
url='http://nxr.northwestern.edu/trep'

pkgname='ros-kinetic-python-trep'
pkgver='1.0.3_2'
pkgrel=1
arch=('any')
license=('GPLv3'
)

makedepends=('freeglut'
'python2'
'python2-matplotlib'
'python2-numpy'
'python2-opengl'
'python2-pillow'
'python2-pyqt4'
'python2-scipy'
'ros-kinetic-catkin'
'ros-kinetic-rospy'
)

depends=('freeglut'
'python2'
'python2-matplotlib'
'python2-numpy'
'python2-opengl'
'python2-pillow'
'python2-pyqt4'
'python2-scipy'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=python_trep
source=()
md5sums=()

prepare() {
    cp -R $startdir/python_trep $srcdir/python_trep
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

